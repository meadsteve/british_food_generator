# British Food Generator
[![Build Status](https://travis-ci.org/meadsteve/british_food_generator.svg?branch=master)](https://travis-ci.org/meadsteve/british_food_generator)

[british-food-generator.herokuapp.com](https://british-food-generator.herokuapp.com)

Written after a conversation at work made me realise that traditional british food names are a little bit strange. 
Code quality is a bit questionable but the core components are detailed below. Contributions are very welcome.

Powered by fastapi and hosted on heroku

## Name generation
Randomly selects from a few key words and combines with joining words.
[british_food_generator/name_generation.py](/british_food_generator/name_generation.py)

## Description generation
Markov chain based. 
Code here: [british_food_generator/description_generation.py](/british_food_generator/description_generation.py)
Source text: [british_food_generator/real_descriptions_of_food.txt](/british_food_generator/real_descriptions_of_food.txt)
