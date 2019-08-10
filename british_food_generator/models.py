from pydantic import BaseModel


class ClassicBritishDish(BaseModel):
    """
    A tasty and definitely real part of British cuisine
    """

    name: str
    description: str
    """Foo's initial location - instance variable"""

    class Config:
        schema_extra = {
            "examples": [
                {
                    "name": "roasted mash",
                    "description": "Finely mashed potato roasted in lard with a side of veg.",
                }
            ]
        }


class CheeckyNandos(BaseModel):
    """
    Bants
    """
    mate_callum_is_a_legend: bool = True