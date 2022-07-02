import django_filters
from django.utils.timezone import now
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from home.models import ProfileInfoPerDay, Profile
from home.serializers.profile_info_per_day import ProfileInfoPerDaySerializer


class ProfileInfoPerDayViewSet(viewsets.ModelViewSet):
    queryset = ProfileInfoPerDay.objects.all()
    serializer_class = ProfileInfoPerDaySerializer
    http_method_names = ['get', 'list']

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = {'date': ['exact', 'lte'],
                        'weight': ['gt']}

    def list(self, request: Request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset.exists():
            profile = Profile.objects.get(user=self.request.user)
            ProfileInfoPerDay.objects.get_or_create(profile=profile, date=request.query_params.get('date', now()))
            queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data[:7])

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        return queryset.filter(profile__user=self.request.user)
