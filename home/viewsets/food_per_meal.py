import django_filters
from rest_framework import viewsets

from home.models import FoodPerMeal
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
            return
        serializer.save()

    def get_queryset(self):
        return self.queryset.filter(meal__user=self.request.user)
