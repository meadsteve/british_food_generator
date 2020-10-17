import random
from typing import List, Set

from constrained_types import ConstrainedString, add_constraint

from british_food_generator.app_logging import log

_non_food_words = {
    "in",
    "the",
    "and",
    "with",
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
    "up",
}


@add_constraint(lambda s: len(s) > 0, "There was an empty url")
@add_constraint(lambda s: s.startswith("https://"), "The url should start with https")
class ImgUrl(ConstrainedString):
    pass


class ImageGenerator:

    images: List[str] = [
        "https://upload.wikimedia.org/wikipedia/commons/7/77/Pork_pie_on_plate.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Sausage-rolls.jpg/1280px-Sausage-rolls.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/1/18/SpottedDick.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/b/bf/Clotted_cream_%28cropped%29.JPG",
        "https://upload.wikimedia.org/wikipedia/commons/4/4f/One_scotch_egg_%28No_jar_of_Marmite%29.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Homerton_College_-_Shepherd%27s_pie.jpg/1280px-Homerton_College_-_Shepherd%27s_pie.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Hot_cross_buns_-_fig_and_pecan.jpg/1280px-Hot_cross_buns_-_fig_and_pecan.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/4/4a/Flickr_bitboy_204619671--Cucumber_sandwiches_with_tea.jpg",
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

    def image_path(self, food_name: str, food_desc: str) -> ImgUrl:
        candidate_words = {
            word
            for word in food_desc.split(" ") + food_name.split(" ")
            if word not in _non_food_words
        }
        possible_images = [
            image for image in self.images if _matches_words(image, candidate_words)
        ]
        log.info(f"Picking image from {len(possible_images)} candidates")
        return ImgUrl(random.choice(possible_images or self.images))


def _matches_words(image_path: str, words: Set[str]):
    normalised_path = image_path.lower()
    for word in words:
        if word in normalised_path:
            log.debug(f"Matched image on {word}")
            return True
    return False
