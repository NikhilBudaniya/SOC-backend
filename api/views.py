
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from uritemplate import partial
from api.serializers import TodoSerializer
from api.models import Todo
from rest_framework import filters
from rest_framework.generics import ListAPIView


class TodoItemViews(APIView):
    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id=None):
        if id:
            task = Todo.objects.get(id=id)
            serializer = TodoSerializer(task)
            return Response( serializer.data, status=status.HTTP_200_OK)

        else:
            tasks=Todo.objects.all()
            serializer=TodoSerializer(tasks,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)

    def patch(self,request,id=None):
        task=Todo.objects.get(id=id)
        serializer=TodoSerializer(task,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self,request,id=None):
        if id:
            task=get_object_or_404(Todo,id=id)
            task.delete()
            return Response("Task Deleted")
        else:
            tasks=Todo.objects.all()
            tasks.delete()
            return Response("All Tasks Deleted")

class TaskSearch(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^title']
    
    
    
