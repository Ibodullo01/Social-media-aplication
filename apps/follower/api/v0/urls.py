from django.urls import path

from .views import following_create , follower_create

app_name = 'follower_api'

urlpatterns = [
    path('following-create/', following_create, name='following_create'),
    path('follower-create/', follower_create, name='follower_create'),
]