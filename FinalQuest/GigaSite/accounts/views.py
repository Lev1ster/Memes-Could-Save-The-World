from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import mixins
from rest_framework.permissions import AllowAny
from rest_framework import status

from . import serializers

class UserCreateOrListView(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           generics.GenericAPIView):

    serializer_class = serializers.UserSerializer
    permission_classes = [AllowAny]

    def get_queryset(self, *args, **kwargs):
        qs = get_user_model().objects.all()
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            user = serializer.save()

            if user:
                json = serializer.data
                headers = self.get_success_headers(serializer.data)
                
                return Response(
                    json,
                    status=status.HTTP_201_CREATED,
                    headers=headers
                )

    def get(self, request,  *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        sorting = request.GET.get('sorting')
        serializer = self.get_serializer(queryset, many=True)
        data = self._sorted_serializer_data(serializer.data, sorting)
        return Response(data)

    def _sorted_serializer_data(self, data):
            return sorted(data, key=lambda k: k['total_posts'], reverse=True)

class UserView(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = serializers.UserSerializer
    permission_classes = [AllowAny]
    queryset = get_user_model().objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
