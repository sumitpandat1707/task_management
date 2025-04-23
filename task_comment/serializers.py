from rest_framework import serializers
from .models import TaskComment

class TaskCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskComment
        fields = '__all__'
