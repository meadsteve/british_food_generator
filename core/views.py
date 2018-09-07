import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


name_part_ones = ['spotted', 'toad', 'dick', 'toddy', 'beef', 'clotted', 'bangers', 'ham', 'fish', 'fried', 'jellied', 'black']
name_part_twos = ['hole', 'pie', 'wellington', 'mash', 'tiddly', 'eels', 'pudding']
joining_words = ['in the', 'and'] + [''] * 10
suffix = ['in gravy', 'with gravy', 'with chips'] + [''] * 10

def generate_food_name():
    return f"{choose(name_part_ones)} {choose(joining_words)} {choose(name_part_twos)} {choose(suffix)}"

def choose(choices):
    return choices[random.randint(0, len(choices)-1)]


def index(request):
    context = {
        'name': generate_food_name(),
        'description': 'Pastry stuffed with raisins'
    }
    template = loader.get_template('british_food.html')
    return HttpResponse(template.render(context, request))

