import random

name_part_ones = ['spotted', 'toad', 'toddy', 'beef', 'clotted', 'bangers',
                  'ham', 'fish', 'fried', 'jellied', 'black', 'Ploughman\'s',
                  'stottie', 'eccles', 'eaton', 'shepherd\'s']
name_part_twos = ['hole', 'pie', 'wellington', 'mash', 'tiddly', 'eels', 'pudding',
                  'stottie', 'pasty', 'tart', 'crumble', 'dick']
joining_words = ['in the', 'and'] + [''] * 5
suffix = ['in gravy', 'with gravy', 'with chips', 'with mint sauce'] + [''] * 15


def generate_food_name():
    return f"{choose(name_part_ones)} {choose(joining_words)} {choose(name_part_twos)} {choose(suffix)}"


def choose(choices):
    return choices[random.randint(0, len(choices)-1)]