from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny

from home.models import Food
from home.serializers.food import FoodSerializer


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    http_method_names = ['get', 'head', 'list']
    pagination_class = LargeResultsSetPagination
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter]
    search_fields = ['^name']
