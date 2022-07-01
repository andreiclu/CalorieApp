import django_filters
from rest_framework import viewsets

from home.models import ProfileInfoPerDay
from home.serializers.profile_info_per_day import ProfileInfoPerDaySerializer


class ProfileInfoPerDayViewSet(viewsets.ModelViewSet):
    queryset = ProfileInfoPerDay.objects.all()
    serializer_class = ProfileInfoPerDaySerializer
    http_method_names = ['list']

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['date']

    def filter_queryset(self, queryset):
        return queryset.filter(user=self.request.user)
