from django.contrib import admin
from .models import Item, Conversation, Message


admin.site.register(Item)
admin.site.register(Conversation)
admin.site.register(Message)
