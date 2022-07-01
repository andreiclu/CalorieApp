from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny

from home.models import Food
from home.serializers.food import FoodSerializer


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    http_method_names = ['get', 'head', 'list']

    permission_classes = [AllowAny]
    filter_backends = [SearchFilter]
    search_fields = ['^name']

