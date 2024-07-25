from rest_framework import serializers

from apps.chat.models import Room, Message
from django.contrib.auth import get_user_model

User = get_user_model()


class RoomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['name']
