from django.urls import path
from .views import MessageListCreateView

urlpatterns = [
    path('messagez/', MessageListCreateView.as_view(), name='message-list-create'),
]