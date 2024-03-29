from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.login, name='login'),
    path('', views.logout, name='logout'),

    # Task related paths
    path('tasks/', views.TaskListView.as_view(), name = 'task-list'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name = 'task-detail'),
    path('tasks/<int:pk>/update_task/', views.TaskUpdateView.as_view(), name = 'task-update'),
    path('tasks/<int:pk>/delete_task/', views.TaskDeleteView.as_view(), name = 'task-delete'),
    path('tasks/create_task', views.TaskCreateView.as_view(), name = 'task-create'),
]