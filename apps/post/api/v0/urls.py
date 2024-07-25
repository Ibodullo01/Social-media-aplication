from django.urls import path
from .views import post_create , post_update ,post_list, \
    post_delete,comment_create,comment_list,comments_post , \
    comment_update,like_post


app_name = 'post_api'

urlpatterns = [
    path('post-create/', post_create, name='post_create'),
    path('post-list/', post_list, name='post_list'),
    path('post-update/<str:pk>', post_update, name='post_update'),
    path('post-delete/<str:pk>' , post_delete, name='post_delete'),
    path('like-post/' , like_post, name='like_post'),
    path('comment-create/', comment_create, name='comment_create'),
    path('comment-list/', comment_list, name='comment_list'),
    path('comment-post/<str:pk>/', comments_post, name='comments_post'),
    path('comment-update/<str:pk>/', comment_update, name='comment_update'),
    path('comment-delete/<str:pk>/', comments_post, name='comments_post'),







]

