from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Task
from .serializers import TaskSerializer

#all task fetch 
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def list_tasks(request):
    user = request.user

    if hasattr(user, 'role') and user.role == 'admin':
        tasks = Task.objects.all().order_by('-created_at')
    else:
        tasks = Task.objects.filter(assigned_to=user).order_by('-created_at')

    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

# POST create new task
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET task by ID
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def retrieve_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = TaskSerializer(task)
    return Response(serializer.data)

# PUT full update
@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = TaskSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# DELETE task
@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    task.delete()
    return Response({'message': 'Task deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# PATCH status field only
@api_view(['PATCH'])
@permission_classes([permissions.IsAuthenticated])
def update_task_status(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)

    status_value = request.data.get('status')
    if not status_value:
        return Response({'error': 'Status field is required'}, status=status.HTTP_400_BAD_REQUEST)

    task.status = status_value
    task.save()
    return Response({'message': 'Status updated successfully', 'status': task.status})

@api_view(['GET'])
#@permission_classes([permissions.IsAuthenticated])
def tasks_by_user(request, user_id):
    tasks = Task.objects.filter(assigned_to__id=user_id).order_by('-due_date')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
