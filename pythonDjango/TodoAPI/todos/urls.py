from django.urls import path
from .views import TodoListAPIView

urlpatterns = [
    path('todos/', TodoListAPIView.as_view(), name='todo-list'),
]