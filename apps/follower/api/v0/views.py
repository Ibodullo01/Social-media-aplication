from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from apps.follower.models import Follow
from .serializers import FollowingCreateSerializer, FollowerListSerializer

User = get_user_model()


class FollowingCreateAPIView(CreateAPIView):
    serializer_class = FollowingCreateSerializer
    queryset = Follow.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)




class FollowerCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_classes = (FollowingCreateSerializer,)
    queryset = Follow.objects.all()

    def post(self, request, username):
        user = User.objects.filter(username=username).first()
        follow = Follow.objects.filter(follower=user, following=self.request.user).first()
        if not follow:
            return Response({"message": "not found follow user"})
        if not follow.is_following:
            follow.is_following = True
            follow.save()
            return Response({"message": "follow back"})
        return Response({"message": "already following"})


class FollowerListAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    queryset = Follow.objects.all()
    serializer_class = FollowerListSerializer



def get(self, request):
    pass






following_create = FollowingCreateAPIView.as_view()
follower_create = FollowerCreateAPIView.as_view()














