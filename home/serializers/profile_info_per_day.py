from rest_framework import serializers

from home.models import ProfileInfoPerDay


class ProfileInfoPerDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileInfoPerDay
        fields = '__all__'

