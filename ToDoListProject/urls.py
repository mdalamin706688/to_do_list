from django.contrib import admin
from django.urls import path, include
from todoapp.views import show_tasks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_tasks, name='root'),
    path('todoapp/', include('todoapp.urls')),
]
