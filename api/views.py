from django.shortcuts import render, get_object_or_404
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def tasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response({'tasks':serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response({'task':serializer.data},status=status.HTTP_200_OK)

@api_view(['POST'])
def add_task(request):
    data = request.data
    serializer = TaskSerializer(data=data)

    if serializer.is_valide():
        serializer.save()
    return Response({'task':serializer.data},status=status.HTTP_201_CREATED) 

@api_view(['PUT'])
def update_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    data = request.data
    serializer = TaskSerializer(isinstance=task, data=data)

    if serializer.is_valide():
        serializer.save()
    return Response({'task':serializer.data}, status=status.HTTP_200_OK) 

@api_view(['DELETE'])
def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return Response({'details':'Delete method is done!'}, status=status.HTTP_204_NO_CONTENT) 