from django.urls import path, include
from rest_framework import routers

from home.viewsets.food import FoodViewSet
from home.viewsets.food_per_meal import FoodPerMealViewSet
from home.viewsets.meal import MealViewSet
from home.viewsets.profile import ProfileViewSet

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'foods', FoodViewSet)
router.register(r'meals', MealViewSet)
router.register(r'foods-per-meal', FoodPerMealViewSet)
urlpatterns = [
    path('', include(router.urls)),

]
