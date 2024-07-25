from django.contrib import messages
from django.contrib.auth import get_user_model
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, parsers
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView, DestroyAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import IsOwner
from .serilizers import PostCreateSerializer, PostListSerializer, CommentCreateSerializer, PostDeleteSerializer, \
    PostUpdateSerializer, CommentSerializer, CommentUpdateSerializer, PostDetailSerializer
from ...models import Post, Comment, LikedPost

User = get_user_model()

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (parsers.MultiPartParser, parsers.FileUploadParser, parsers.JSONParser)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostUpdateAPIView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
    permission_classes = [IsOwner]

    lookup_field = 'pk'

    def get_object(self):
        obj = super().get_object()
        self.check_object_permissions(self.request, obj)
        return obj

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class PostDetailAPIView(DestroyAPIView):
    queryset = Post.objects.all().prefetch_related('comments__children')
    serializer_class = PostDetailSerializer

    lookup_field = 'pk'


class LikePostAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="description")
    def post(self, request):
        post_id = request.data.get('id')
        if not post_id:
            return Response({'error': 'Post ID is required'}, status=status.HTTP_400_BAD_REQUEST)

        post = get_object_or_404(Post, id=post_id)
        liked_post = LikedPost.objects.filter(post=post, user=request.user).first()

        if liked_post:
            liked_post.delete()
            return Response({'message': 'Disliked'}, status=status.HTTP_204_NO_CONTENT)

        LikedPost.objects.create(post=post, user=request.user)
        return Response({'message': 'Liked post'}, status=status.HTTP_201_CREATED)

class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDeleteSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        post = get_object_or_404(Post, id=pk)

        if request.user != post.user:
            return Response({'detail': 'You do not have permission to delete this post.'}, status=status.HTTP_403_FORBIDDEN)

        post.delete()
        messages.success(request, 'Post deleted successfully')
        return Response({'detail': 'Post deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = (IsAuthenticated ,)

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)

class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        comment = get_object_or_404(Comment, id=pk)
        self.check_object_permissions(self.request, comment)
        return comment

class CommentPostListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = get_object_or_404(Post, id=self.kwargs.get('pk'))
        return Comment.objects.filter(post=post_id , parent__isnull=True)

class CommentUpdateAPIView(UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get('pk')
        comment = get_object_or_404(Comment, id=pk)
        self.check_object_permissions(self.request, comment)
        return comment

class CommentDeleteAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    permission_classes = [
    IsAuthenticated,IsOwner
    ]

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        comment = get_object_or_404(Comment, id=pk)
        if request.user != comment.post.user:
            return Response({"detail": "You do not have permission to delete this comment."},)
        else:
            comment.delete()
            return Response({'detail': 'comment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

like_post = LikePostAPIView.as_view()
post_detail = PostDetailAPIView.as_view()
post_list = PostListAPIView.as_view()
post_update = PostUpdateAPIView.as_view()
post_create = PostCreateAPIView.as_view()
post_delete = PostDeleteAPIView.as_view()
comment_list = CommentListAPIView.as_view()
comments_post = CommentPostListAPIView.as_view()
comment_create = CommentCreateAPIView.as_view()
comment_update = CommentUpdateAPIView.as_view()
comment_delete = CommentDeleteAPIView.as_view()


