from constrained_types import add_constraint, ConstrainedString
from pydantic import BaseModel


@add_constraint(lambda s: len(s) > 0, "There was an empty url")
@add_constraint(lambda s: s.startswith("https://"), "The url should start with https")
class ImgUrl(ConstrainedString):
    pass


@add_constraint(lambda s: len(s) > 0, "The description should not be empty")
class FoodDescription(ConstrainedString):
    pass


@add_constraint(lambda s: len(s) > 0, "The name should not be empty")
class FoodName(ConstrainedString):
    pass


class ClassicBritishDish(BaseModel):
    """
    A tasty and definitely real part of British cuisine
    """

    name: FoodName
    description: FoodDescription
    image: ImgUrl

    class Config:
        schema_extra = {
            "examples": [
                {
                    "name": "roasted mash",
                    "description": "Finely mashed potato roasted in lard with a side of veg.",
                    "image": "https://upload.wikimedia.org/wikipedia/commons/7/77/Pork_pie_on_plate.jpg",
                }
            ]
        }


class CheeckyNandos(BaseModel):
    """
    Bants
    """

    mate_callum_is_a_legend: bool = True
