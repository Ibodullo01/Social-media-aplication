from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from .serilizers import UserCreateSerializer, UsersListSerializer

User = get_user_model()

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = (AllowAny , )



class UsersListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersListSerializer
    permission_classes = (AllowAny , )

get_users = UsersListAPIView.as_view()
user_create = UserCreateAPIView.as_view()
