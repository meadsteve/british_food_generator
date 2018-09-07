from django.http import HttpResponse

# Create your views here.
from django.template import loader

from core.name_generation import generate_food_name

def index(request):
    context = {
        'name': generate_food_name(),
        'description': 'Pastry stuffed with raisins'
    }
    template = loader.get_template('british_food.html')
    return HttpResponse(template.render(context, request))

