import os

from fastapi import FastAPI
from lagom import Singleton, bind_to_container, injectable
from lagom.integrations.fast_api import FastApiContainer
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from british_food_generator.monitoring.asyncio import Monitor
from british_food_generator.complete_dish import CompleteDishBuilder
from british_food_generator.description_generation import FoodDescriber
from british_food_generator.meta import VERSION, DESCRIPTION
from british_food_generator.models import ClassicBritishDish, CheeckyNandos

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

app = FastAPI(title="British Food Generator", version=VERSION, description=DESCRIPTION)

container = FastApiContainer()

# The describer is built on startup as it may take a while to scan the  file
container[FoodDescriber] = FoodDescriber(
    os.path.join(__location__, "real_descriptions_of_food.txt")
)

# These other components can be singletons but we can defer creation until they are need the first time
container[CompleteDishBuilder] = Singleton(CompleteDishBuilder)
container[Jinja2Templates] = Singleton(lambda: Jinja2Templates(directory="templates"))
container[Monitor] = Singleton(lambda: Monitor(interval=0.25))


@app.on_event("startup")
@bind_to_container(container)
def start_monitoring(monitor: Monitor = injectable):
    monitor.start()


@app.get("/", include_in_schema=False)
def read_root(
    request: Request,
    builder=container.depends(CompleteDishBuilder),
    templates=container.depends(Jinja2Templates),
):
    dish = builder.generate_dish()
    return templates.TemplateResponse(
        "british_food.html",
        {
            "name": dish.name,
            "description": dish.description,
            "background_image": dish.image,
            "request": request,
        },
    )


@app.get(
    "/api",
    response_model=ClassicBritishDish,
    summary="The latest British Dishes",
    description="Calling this endpoint will return a randomly selected totally legitimate British dish.",
    responses={
        "418": {
            "model": CheeckyNandos,
            "description": "Shall we go for a cheeky nandos?",
        }
    },
)
def raw(builder=container.depends(CompleteDishBuilder)):
    return builder.generate_dish()


@app.get("/health", summary="Stats on the health of the system")
def health(monitor=container.depends(Monitor)):
    return {
        "healthy": True,
        "async_lag_ms": monitor.lag * 1_000,
        "active_tasks": monitor.active_tasks,
    }


@app.get("/debug", summary="raw tech data on how the service is working")
def debug():
    return {
        "container": {
            "reflection": container.reflection_cache_overview,
            "definitions": [t.__qualname__ for t in container.defined_types],
        }
    }


# If no other route matches assume that it might be a static file
app.mount("/", StaticFiles(directory="static_assets"), name="static")
