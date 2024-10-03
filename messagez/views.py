# from django.shortcuts import render
from rest_framework import generics
from .models import Message
from .serializers import MessageSerializer


class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all().order_by("-timestamp")
    serializer_class = MessageSerializer


class MessageDeleteView(generics.DestroyAPIVew):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
