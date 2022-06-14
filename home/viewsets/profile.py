from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response

from home.models import Profile
from home.serializers.profile import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_names = ['get', 'put', 'patch', 'head']

    def list(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=request.user)

        serializer = self.get_serializer(profile)
        return Response(serializer.data)

    def filter_queryset(self, queryset):
        return queryset.filter(user=self.request.user)

