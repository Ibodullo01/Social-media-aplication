from django.contrib import admin

from apps.chat.models import Room, Message

admin.site.register([Room , Message])
