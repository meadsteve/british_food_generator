import os
import markovify


class FoodDescriber:
    def __init__(self, file_path):
        with open(file_path) as f:
            text = f.read()
        self._text_model = markovify.NewlineText(text, state_size=2)

    def generate_food_description(self):
        return self._text_model.make_short_sentence(200, tries=100)


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

food_describer = FoodDescriber(
    os.path.join(__location__, "real_descriptions_of_food.txt")
)
