from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.dispatch import receiver

from .models import Follow
from apps.notification.models import Notification

User = get_user_model()


@receiver(post_save, sender=Follow)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.following,
            content_type=ContentType.objects.get_for_model(instance),
            object_id=instance.pk,
            message="You have been followed",

        )