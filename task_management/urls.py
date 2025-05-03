from django.contrib import admin
from django.urls import path, include
from django.conf import settings                          # ✅ Add this line
from django.conf.urls.static import static                # ✅ Already there

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),
    path('api/tasks/', include('tasks.urls')),
    path('api/', include('task_comment.urls')),
    path('api/', include('project.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
