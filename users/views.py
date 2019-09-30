from rest_framework.generics import CreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from users.serializers import UserCreateSerializer, UserUpdateSerializer
from users import models


class CreateUserApiView(CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = UserCreateSerializer


class UpdateUserApiView(UpdateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = UserUpdateSerializer
    lookup_url_kwarg = 'user_id'
    queryset = models.User.objects.all()
