from fastapi import FastAPI, Depends
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from british_food_generator.description_generation import food_describer
from british_food_generator.meta import VERSION, DESCRIPTION
from british_food_generator.models import ClassicBritishDish, CheeckyNandos
from british_food_generator.name_generation import generate_food_name

app = FastAPI(title="British Food Generator", version=VERSION, description=DESCRIPTION)

templates = Jinja2Templates(directory="templates")


@app.get("/", include_in_schema=False)
def read_root(
    request: Request,
    food_name: str = Depends(generate_food_name),
    food_desc: str = Depends(food_describer.generate_food_description),
):
    return templates.TemplateResponse(
        "british_food.html",
        {"name": food_name, "description": food_desc, "request": request},
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
    food_name: str = Depends(generate_food_name),
    food_desc: str = Depends(food_describer.generate_food_description),
):
    return {"name": food_name, "description": food_desc}
