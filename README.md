# British Food Generator
[![Build Status](https://travis-ci.org/meadsteve/british_food_generator.svg?branch=master)](https://travis-ci.org/meadsteve/british_food_generator)

[british-food-generator.herokuapp.com](https://british-food-generator.herokuapp.com)

Written after a conversation at work made me realise that traditional british food names are a little bit strange. 
Code quality is a bit questionable but the core components are detailed below. Contributions are very welcome.

Powerd by django (but using almost none of django's features) and hosted on heroku

## Name generation
Randomly selects from a few key words and combines with joining words.
[core/name_generation.py](/core/name_generation.py)

## Description generation
Markov chain based. 
Code here: [core/description_generation.py](/core/description_generation.py)
Source text: [core/real_descriptions_of_food.txt](/core/real_descriptions_of_food.txt)
