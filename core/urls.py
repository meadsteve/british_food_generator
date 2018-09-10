from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('food/<str:encoded_food_name>/<str:encoded_description>/', views.existing, name='existing'),
]