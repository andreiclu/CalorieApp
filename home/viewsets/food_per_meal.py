import django_filters
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

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
        serializer.save()

    def get_queryset(self):
        return self.queryset.filter(meal__user=self.request.user)
