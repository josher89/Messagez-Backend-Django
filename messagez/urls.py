from django.urls import path
from .views import MessageListCreateView, MessageDeleteView

urlpatterns = [
    path("messagez/", MessageListCreateView.as_view(), name="message-list-create"),
    path("messagez/<int:pk>/", MessageDeleteView.as_view(), name="message-delete"),
]
