import os
import markovify

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'real_descriptions_of_food.txt')) as f:
    text = f.read()
text_model = markovify.NewlineText(text)

def generate_food_description():
    return text_model.make_short_sentence(140)