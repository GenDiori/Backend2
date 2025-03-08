from django.urls import path
from .views import (
    thread_list, thread_detail, thread_delete, thread_edit,
    post_delete, post_edit
)

urlpatterns = [
    path('', thread_list, name='thread-list'),  # Просто '', так как 'threads/' уже добавлен в главном urls.py
    path('<int:pk>/', thread_detail, name='thread-detail'),
    path('<int:pk>/delete/', thread_delete, name='thread-delete'),
    path('<int:pk>/edit/', thread_edit, name='thread-edit'),
    path('posts/<int:pk>/delete/', post_delete, name='post-delete'),
    path('posts/<int:pk>/edit/', post_edit, name='post-edit'),
]
