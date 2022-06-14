from rest_framework import routers, serializers, viewsets

from home.models import Meal


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        exclude = ['user']
