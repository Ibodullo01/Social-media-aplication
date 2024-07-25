from rest_framework import serializers

from apps.follower.models import Follow


class FollowingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['following']

class FollowerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['follower']

