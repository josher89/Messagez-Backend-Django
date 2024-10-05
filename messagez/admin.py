from django.contrib import admin
from .models import Message, MessagePerson

admin.site.register(Message)
admin.site.register(MessagePerson)
