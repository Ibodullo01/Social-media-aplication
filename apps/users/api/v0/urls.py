from django.urls import path
from .views import user_create,get_users

app_name = 'users_api'

urlpatterns = [
    path('create/', user_create, name='user_create'),
    path('users/', get_users, name='get_users'),

]

