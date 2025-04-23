from django.contrib import admin
from .models import TaskComment

@admin.register(TaskComment)
class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'task', 'comment', 'created_at', 'updated_at']
    list_filter = ['task', 'created_at']
    search_fields = ['comment', 'task__title']
    ordering = ['-created_at']
