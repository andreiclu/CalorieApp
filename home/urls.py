
from django.urls import path, include
from rest_framework import routers

from home.viewsets.food import FoodViewSet
from home.viewsets.food_per_meal import FoodPerMealViewSet
from home.viewsets.meal import MealViewSet
from home.viewsets.profile import ProfileViewSet
from home.viewsets.profile_info_per_day import ProfileInfoPerDayViewSet

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'foods', FoodViewSet)
router.register(r'meals', MealViewSet)
router.register(r'foods-per-meal', FoodPerMealViewSet)
router.register(r'profile-info-per-day', ProfileInfoPerDayViewSet)
urlpatterns = [
    path('', include(router.urls)),

]



