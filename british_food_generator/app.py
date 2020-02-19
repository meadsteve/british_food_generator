import os

from fastapi import FastAPI
from lagom import Singleton
from lagom.integrations.fast_api import FastApiContainer
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from british_food_generator.monitoring.asyncio import Monitor
from british_food_generator.complete_dish import CompleteDishBuilder
from british_food_generator.description_generation import FoodDescriber
from british_food_generator.meta import VERSION, DESCRIPTION
from british_food_generator.models import ClassicBritishDish, CheeckyNandos

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

monitor = Monitor(0.25)
app = FastAPI(title="British Food Generator", version=VERSION, description=DESCRIPTION)

templates = Jinja2Templates(directory="templates")

container = FastApiContainer()
container[FoodDescriber] = FoodDescriber(
    os.path.join(__location__, "real_descriptions_of_food.txt")
)
container[CompleteDishBuilder] = Singleton(CompleteDishBuilder)


@app.on_event("startup")
def start_monitoring():
    monitor.start()


@app.get("/", include_in_schema=False)
def read_root(request: Request, builder=container.depends(CompleteDishBuilder)):
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
def health():
    return {
        "healthy": True,
        "async_lag_ms": monitor.lag * 1_000,
        "active_tasks": monitor.active_tasks
    }
