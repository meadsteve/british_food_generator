import os

from fastapi import FastAPI
from lagom.integrations.fast_api import FastApiContainer
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from british_food_generator.description_generation import FoodDescriber
from british_food_generator.image_generation import ImageGenerator
from british_food_generator.name_generation import FoodNamer
from british_food_generator.meta import VERSION, DESCRIPTION
from british_food_generator.models import ClassicBritishDish, CheeckyNandos

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

app = FastAPI(title="British Food Generator", version=VERSION, description=DESCRIPTION)

templates = Jinja2Templates(directory="templates")

container = FastApiContainer()
container[FoodDescriber] = FoodDescriber(
    os.path.join(__location__, "real_descriptions_of_food.txt")
)
container[FoodNamer] = FoodNamer()
container[ImageGenerator] = ImageGenerator()


@app.get("/", include_in_schema=False)
def read_root(
    request: Request,
    namer=container.depends(FoodNamer),
    describer=container.depends(FoodDescriber),
    imager=container.depends(ImageGenerator)
):
    name = namer.generate_food_name()
    desc = describer.generate_food_description()
    return templates.TemplateResponse(
        "british_food.html",
        {
            "name": name,
            "description": desc,
            "background_image": imager.image_path(name, desc),
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
def raw(
    namer=container.depends(FoodNamer),
    describer=container.depends(FoodDescriber),
    imager=container.depends(ImageGenerator)
):
    name = namer.generate_food_name()
    desc = describer.generate_food_description()
    return ClassicBritishDish(
        name=name,
        description=desc,
        image=imager.image_path(name, desc)
    )
