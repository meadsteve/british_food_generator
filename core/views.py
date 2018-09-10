from base64 import urlsafe_b64encode, urlsafe_b64decode

from django.http import HttpResponse

from django.template import loader

from core.description_generation import generate_food_description
from core.name_generation import generate_food_name


def _encode(string_data: str):
    return urlsafe_b64encode(bytearray(string_data.encode("utf-8"))).decode("utf-8")


def _decode(data):
    return urlsafe_b64decode(data).decode("utf-8")


def _build_permalink(request, food_name, description):
    perma_link = request.build_absolute_uri(
        f"/food/{_encode(food_name)}/{_encode(description)}/"
    )
    return perma_link


def _render_food_page(request, food_name, description):
    perma_link = _build_permalink(request, food_name, description)
    context = {"name": food_name, "description": description, "perma_link": perma_link}
    template = loader.get_template("british_food.html")
    return template.render(context, request)


def index(request):
    food_name = generate_food_name().capitalize()
    description = generate_food_description()
    return HttpResponse(_render_food_page(request, food_name, description))


def existing(request, encoded_food_name, encoded_description):
    food_name = _decode(encoded_food_name)
    description = _decode(encoded_description)
    return HttpResponse(_render_food_page(request, food_name, description))
