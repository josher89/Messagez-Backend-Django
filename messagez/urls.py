from django.urls import path
from .views import MessageListCreateView, MessageDeleteView, MessagePersonListCreateView, MessagePersonDeleteView

urlpatterns = [
    path("messagez/", MessageListCreateView.as_view(), name="message-list-create"),
    path("messagez/<int:pk>/", MessageDeleteView.as_view(), name="message-delete"),
    path("messagez/person", MessagePersonListCreateView.as_view(), name="messageperson-list-create"),
    path("messagez/person/<int:pk>/", MessagePersonDeleteView.as_view(), name="messageperson-delete"),
]
