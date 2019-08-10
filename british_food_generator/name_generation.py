import random
from typing import List, TypeVar


def one_of_in_x_times(choices: List[str], times: int) -> List[str]:
    return choices + ([""] * (times - 1) * len(choices))


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
    "roast",
    "pickled",
    "soused",
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
    "roast",
]

joining_words = one_of_in_x_times(["in the", "and", "cream"], times=3)
suffix = one_of_in_x_times(
    [
        "in gravy",
        "with gravy",
        "with chips",
        "with mint sauce",
        "with custard",
        "in blankets",
    ],
    times=4,
)

# Items which are either boring or rude should be excluded
banned_list = ["spotted dick", "fish pie"]


def generate_food_name() -> str:
    result = None
    while result in banned_list or result is None:
        result = f"{choose(name_part_ones)} {choose(joining_words)} {choose(name_part_twos)} {choose(suffix)}".strip()
    return result
