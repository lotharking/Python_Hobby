from .serializers import TodoSerializer
from .models import Todo
from rest_framework import generics

class TodoListAPIView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer