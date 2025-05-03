# tasks/models.py

from django.db import models
from django.conf import settings
from project.models import Project  # 👈 Import Project model

PRIORITY_CHOICES = (
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
)

STATUS_CHOICES = (
    ('To Do', 'To Do'),
    ('In Progress', 'In Progress'),
    ('Pending', 'Pending'),  # ✅ Fix capitalization
    ('Completed', 'Completed'),
)

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)# 👈 Add project field
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks'
    )
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='To Do')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
