from starlette.testclient import TestClient

from british_food_generator.app import app
from british_food_generator.description_generation import generate_food_description
from british_food_generator.name_generation import generate_food_name


def test_food_name_is_a_string():
    assert type(generate_food_name()) == str


def test_food_description_is_a_string():
    assert type(generate_food_description()) == str


client = TestClient(app)


def test_app_serves_some_html_at_the_root():
    response = client.get("/")
    assert response.status_code == 200
    assert b"The latest British Dishes" in response.content


def test_app_api_end_point_serves_some_json():
    response = client.get("/api")
    assert response.status_code == 200
    json = response.json()
    assert "name" in json
    assert "description" in json
