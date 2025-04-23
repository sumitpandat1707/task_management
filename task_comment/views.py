from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TaskComment
from .serializers import TaskCommentSerializer

@api_view(['GET'])
def get_comments_by_task(request, task_id):
    comments = TaskComment.objects.filter(task_id=task_id)
    serializer = TaskCommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_comment(request):
    serializer = TaskCommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_comment(request, pk):
    try:
        comment = TaskComment.objects.get(pk=pk)
    except TaskComment.DoesNotExist:
        return Response({"error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = TaskCommentSerializer(comment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_comment(request, pk):
    try:
        comment = TaskComment.objects.get(pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except TaskComment.DoesNotExist:
        return Response({"error": "Comment not found"}, status=status.HTTP_404_NOT_FOUND)
