import logging
import random
from typing import List, Set

log = logging.getLogger(__name__)


_non_food_words = {
    "in",
    "the",
    "and",
    "with"
    "but",
    "or",
    "a",
    "out",
    "is",
    "to",
    "on",
    "as",
    "an",
    "at",
    "up"
}


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
        "https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/Chorley_cake_and_Eccles_cake.jpg/1920px-Chorley_cake_and_Eccles_cake.jpg",
    ]

    def image_path(self, food_name: str, food_desc: str) -> str:
        candidate_words = set([word for word in food_desc.split(" ") + food_name.split(" ") if word not in _non_food_words])
        possible_images = [image for image in self.images if _matches_words(image, candidate_words)]
        log.info(f"Picking image from {len(possible_images)} candidates")
        return random.choice(possible_images or self.images)


def _matches_words(image_path: str, words: Set[str]):
    normalised_path = image_path.lower()
    for word in words:
        if word in normalised_path:
            log.debug(f"Matched image on {word}")
            return True
    return False
