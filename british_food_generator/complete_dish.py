from british_food_generator.description_generation import FoodDescriber
from british_food_generator.image_generation import ImageGenerator
from british_food_generator.models import ClassicBritishDish
from british_food_generator.name_generation import FoodNamer


class CompleteDishBuilder:
    def __init__(
        self, namer: FoodNamer, describer: FoodDescriber, imager: ImageGenerator
    ):
        self.namer = namer
        self.describer = describer
        self.imager = imager

    def generate_dish(self) -> ClassicBritishDish:
        name = self.namer.generate_food_name()
        desc = self.describer.generate_food_description(name)
        image = self.imager.image_path(name, desc)
        return ClassicBritishDish(name=name, description=desc, image=image)
