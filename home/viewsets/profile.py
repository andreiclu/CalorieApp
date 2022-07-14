
from rest_framework import viewsets
from rest_framework.response import Response

from home.models import Profile
from home.serializers.profile import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    http_method_names = ['get', 'put', 'patch', 'head', 'post']

    def list(self, request, *args, **kwargs):
        profile, created = Profile.objects.get_or_create(user=request.user)

        serializer = self.get_serializer(profile)
        return Response(serializer.data)

    def filter_queryset(self, queryset):
        return queryset.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        profile = Profile.objects.get(user=self.request.user)
        data = dict(request.data)
        data["user"] = self.request.user.pk
        serializer = self.get_serializer(profile, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

