from fastapi import FastAPI, Depends
from pydantic import BaseModel
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from british_food_generator.description_generation import generate_food_description
from british_food_generator.name_generation import generate_food_name

app = FastAPI()

templates = Jinja2Templates(directory="templates")


class ClassicBritishDish(BaseModel):
    """
    A tasty and definitely real part of British cuisine
    """

    name: str
    description: str
    """Foo's initial location - instance variable"""

    class Config:
        schema_extra = {
            'examples': [
                {
                    "name": "roasted mash",
                    "description": "Finely mashed potato roasted in lard with a side of veg.",
                }
            ]
        }


@app.get("/", include_in_schema=False)
def read_root(
    request: Request,
    food_name: str = Depends(generate_food_name),
    food_desc: str = Depends(generate_food_description),
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
)
def raw(
    food_name: str = Depends(generate_food_name),
    food_desc: str = Depends(generate_food_description),
):
    return {"name": food_name, "description": food_desc}
