from typing import List

import markovify

from british_food_generator.app_logging import log

_exclude_words = {
    "in",
    "the",
    "and",
    "with",
}


class FoodDescriber:
    def __init__(self, file_path):
        with open(file_path) as f:
            text = f.read()
        self._text_model = markovify.Text(text)

    def generate_food_description(self, name: str):
        name_words = [
            word for word in name.lower().split(" ") if word not in _exclude_words
        ]

        sample = (self._desc_at_total_random() for _ in range(0, 500))
        scored_samples = (
            (desc, self._score_description(desc, name_words)) for desc in sample
        )
        sorted_samples = sorted(scored_samples, key=lambda x: x[1])
        best_fit = sorted_samples[0]

        log.info(f"Returning a description with a score of {best_fit[1]}")
        return best_fit[0]

    def _desc_at_total_random(self):
        return self._text_model.make_short_sentence(200, tries=100)

    @staticmethod
    def _score_description(desc: str, name_words: List[str]) -> float:
        # We want a description that mentions the name but
        # not too often. So a perfect score is mentioning
        # the title either 3 or 4 times
        word_matches = sum(desc.lower().count(word) for word in name_words)
        return abs(3.5 - word_matches)
