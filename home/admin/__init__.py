from django.contrib import admin

from home.models import Meal, FoodPerMeal
from . import food
from . import profile

admin.site.register(Meal)
admin.site.register(FoodPerMeal)
