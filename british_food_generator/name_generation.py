import random
from typing import List, TypeVar, Set


def one_of_in_x_times(choices: Set[str], times: int) -> List[str]:
    return list(choices) + ([""] * (times - 1) * len(choices))


T = TypeVar("T")


def choose(choices: List[T]) -> T:
    return random.choice(choices)


class FoodNamer:

    name_part_ones = list(
        {
            "cucumber",
            "corned",
            "custard",
            "treacle",
            "spotted",
            "toad",
            "toddy",
            "beef",
            "clotted",
            "bangers",
            "ham",
            "fish",
            "fried",
            "jellied",
            "black",
            "ploughman's",
            "stottie",
            "eccles",
            "eton",
            "shepherd's",
            "knickerbocker",
            "angel",
            "lardy",
            "jam",
            "bubble",
            "stargazy",
            "boiled",
            "lancashire",
            "devonshire",
            "welsh",
            "roast",
            "pickled",
            "soused",
            "scotch",
        }
    )

    name_part_twos = list(
        {
            "hole",
            "pie",
            "wellington",
            "mash",
            "tiddly",
            "eels",
            "pudding",
            "stottie",
            "pasty",
            "tart",
            "crumble",
            "dick",
            "glory",
            "delight",
            "cake",
            "beef",
            "rolly polly",
            "scratchings",
            "squeak",
            "roast",
            "rarebit",
            "sandwich",
            "egg",
        }
    )

    joining_words = one_of_in_x_times({"in the", "and", "cream"}, times=3)
    suffix = one_of_in_x_times(
        {
            "in gravy",
            "with gravy",
            "with chips",
            "with mint sauce",
            "with custard",
            "in blankets",
        },
        times=4,
    )

    def generate_food_name(self) -> str:
        return _tidy_name(
            f"{choose(self.name_part_ones)} {choose(self.joining_words)} {choose(self.name_part_twos)} {choose(self.suffix)}"
        )


def _tidy_name(food_name: str) -> str:
    return food_name.strip().replace("  ", " ")
