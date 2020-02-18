from pydantic import BaseModel


class ClassicBritishDish(BaseModel):
    """
    A tasty and definitely real part of British cuisine
    """

    name: str
    description: str
    image: str

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
