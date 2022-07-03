import django_filters
from rest_framework import viewsets

from home.models import FoodPerMeal, ProfileInfoPerDay
from home.serializers.food_per_meal import FoodPerMealSerializer, CreateFoodPerMealSerializer


class FoodPerMealViewSet(viewsets.ModelViewSet):
    queryset = FoodPerMeal.objects.all()
    serializer_class = FoodPerMealSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['meal']

    def get_serializer_class(self):
        if self.action == 'create':
            return CreateFoodPerMealSerializer
        return FoodPerMealSerializer

    def perform_create(self, serializer):
        existing = FoodPerMeal.objects.filter(meal=serializer.validated_data['meal'],
                                              food=serializer.validated_data['food']).first()
        if existing:
            existing.number += serializer.validated_data['number']
            existing.save()
        else:
            serializer.save()
        food = serializer.validated_data['food']
        number = serializer.validated_data['number']
        profile_info_per_day, created = ProfileInfoPerDay.objects.get_or_create(profile__user=self.request.user,
                                                                                date=serializer.validated_data[
                                                                                    'meal'].date)
        profile_info_per_day.calories += number * food.calories
        profile_info_per_day.proteins += number * food.protein
        profile_info_per_day.fats += number * food.total_fats
        profile_info_per_day.carbs += number * food.carbohydrate
        profile_info_per_day.save()

        meal = serializer.validated_data['meal']
        meal.calories += number * food.calories
        meal.proteins += number * food.protein
        meal.fats += number * food.total_fats
        meal.carbs += number * food.carbohydrate
        meal.save()


    def get_queryset(self):
        return self.queryset.filter(meal__user=self.request.user)
