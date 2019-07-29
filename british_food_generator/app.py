from fastapi import FastAPI, Depends
from starlette.requests import Request
from starlette.templating import Jinja2Templates

from british_food_generator.description_generation import generate_food_description
from british_food_generator.name_generation import generate_food_name

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def read_root(
    request: Request,
    food_name: str = Depends(generate_food_name),
    food_desc: str = Depends(generate_food_description),
):
    return templates.TemplateResponse(
        "british_food.html",
        {"name": food_name, "description": food_desc, "request": request},
    )


@app.get("/raw")
def raw(
    food_name: str = Depends(generate_food_name),
    food_desc: str = Depends(generate_food_description),
):
    return {"name": food_name, "description": food_desc}
