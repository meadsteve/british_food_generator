import random
from typing import List, TypeVar


def one_of_in_x_times(list: List[str], times: int) -> List[str]:
    return list + ([""] * (times - 1) * len(list))


T = TypeVar("T")


def choose(choices: List[T]) -> T:
    return choices[random.randint(0, len(choices) - 1)]


name_part_ones = [
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
    "eaton",
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
]
name_part_twos = [
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
    "rolly polly",
    "scratchings",
    "squeak",
]

joining_words = one_of_in_x_times(["in the", "and"], times=3)
suffix = one_of_in_x_times(
    ["in gravy", "with gravy", "with chips", "with mint sauce"], times=4
)


def generate_food_name() -> str:
    return f"{choose(name_part_ones)} {choose(joining_words)} {choose(name_part_twos)} {choose(suffix)}"
