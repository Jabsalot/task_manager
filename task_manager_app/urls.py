from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),

    # TASKS
    path('tasks/', views.TaskListView.as_view(), name = 'task-list'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name = 'task-detail'),
    path('tasks/<int:pk>/update_task/', views.TaskUpdateView.as_view(), name = 'task-update'),
    path('tasks/<int:pk>/delete_task/', views.TaskDeleteView.as_view(), name = 'task-delete'),
    path('tasks/create_task<int:team_member_id>', views.TaskCreateView.as_view(), name = 'task-create'),

    # SET UP ROLE WITHIN TEAM
    path('create_team/', views.createTeamPage, name = 'create-team-page'),
    path('join_team/', views.joinTeamPage, name = 'join-team-page'),

    # TEAM LEAD PAGES
    path('team_lead/', views.teamLeadPage, name = 'team-lead-page'),
    path('team_lead/<int:team_member_id>/', views.getTeamMemberTasks, name = 'team-member-tasks'),
    path('team_lead/<int:team_member_id>/create_task/', views.createTask, name = 'task-create-page'),

    # TEAM MEMBER PAGES
    path('team_member', views.teamMemberPage, name = 'team-member-page'),
    path('team_member/<int:task_id>/', views.getTaskInfo, name = 'team-member-task-info'),
   
    # USER ACCOUNTS AND AUTHENTICATION PAGES
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.registerPage, name = 'register-page'),
]