import random
from typing import List


class ImageGenerator:

    images: List[str] = [
        "https://upload.wikimedia.org/wikipedia/commons/7/77/Pork_pie_on_plate.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Sausage-rolls.jpg/1280px-Sausage-rolls.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/1/18/SpottedDick.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/6/62/Christmas_pudding.JPG",
        "https://upload.wikimedia.org/wikipedia/commons/0/01/Toad_in_the_hole.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/1/1d/Bangers_and_Mash_%28vegan_version%29.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Stornoway_Black_Pudding.jpg/1024px-Stornoway_Black_Pudding.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Oatcakes_%281%29.jpg/1920px-Oatcakes_%281%29.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/4/4b/YorkShireParkin.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Englishbreakfast.jpg/1280px-Englishbreakfast.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Cornish_cream_tea_2.jpg/1280px-Cornish_cream_tea_2.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Chorley_cake_and_Eccles_cake.jpg/1920px-Chorley_cake_and_Eccles_cake.jpg"
    ]

    def image_path(self, _food_name: str, _food_desc: str) -> str:
        # TODO: something cleverer than picking at random
        return random.choice(self.images)
