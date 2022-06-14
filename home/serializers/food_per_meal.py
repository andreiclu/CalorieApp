from rest_framework import routers, serializers, viewsets

from home.models import FoodPerMeal


class FoodPerMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodPerMeal
        fields = '__all__'
        depth = 1


class CreateFoodPerMealSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodPerMeal
        fields = '__all__'
