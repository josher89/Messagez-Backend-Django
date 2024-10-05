# from django.shortcuts import render
from rest_framework import generics
from .models import Message, MessagePerson
from .serializers import MessageSerializer, MessagePersonSerializer


class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all().order_by("-timestamp")
    serializer_class = MessageSerializer


class MessageDeleteView(generics.DestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessagePersonListCreateView(generics.ListCreateAPIView):
    queryset = MessagePerson.objects.all()
    serializer_class = MessagePersonSerializer


class MessagePersonDeleteView(generics.DestroyAPIView):
    queryset = MessagePerson.objects.all()
    serializer_class = MessagePersonSerializer