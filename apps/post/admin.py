from django.contrib import admin

from apps.post.models import *

# Register your models here.

admin.site.register([Post , PostImage , LikedPost , Tag , Comment, LikedComment ])