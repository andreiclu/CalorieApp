from rest_framework import routers, serializers, viewsets

from home.models import Profile, Food


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

