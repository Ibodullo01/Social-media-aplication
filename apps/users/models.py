from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='media/', blank=True)
    phone = models.CharField(max_length=20, null=True)
    bio = models.TextField(max_length=500, blank=True)
    brith_date = models.DateField(null=True)
    location = models.URLField(null=True , blank=True , max_length=100 )

    def __str__(self):
        return self.username


class ProfileImage(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    image = models.ImageField(upload_to='media/', blank=True)

    def __str__(self):
        return f"{self.user.username}'s picture"



