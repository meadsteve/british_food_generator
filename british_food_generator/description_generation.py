import random

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
        self._text_model = markovify.NewlineText(text, state_size=2)

    def generate_food_description(self, name: str):
        try:
            # Try and markov with a word from the name
            start_word = random.choice(
                [word for word in name.split(" ") if word not in _exclude_words]
            )
            log.info(
                f"Attempting to use the word '{start_word}' to build a description"
            )
            desc = self._text_model.make_sentence_with_start(start_word, strict=False)
            return desc or self._desc_at_total_random()
        except:
            # If anything goes wrong just describe something at random
            return self._desc_at_total_random()

    def _desc_at_total_random(self):
        log.info("Falling back to totally random description")
        return self._text_model.make_short_sentence(200, tries=100)
