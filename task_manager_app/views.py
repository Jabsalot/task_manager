from .models import *
from .forms import *
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import Group

###########################################################
#                    CLASS BASED MODELS                   #
###########################################################

''' Queries database to gather all tasks '''
class TaskListView(generic.ListView):
    model = Task

''' Queries database to gather task details '''
class TaskDetailView(generic.DetailView):
    model = Task

''' Queries database to gather task details to update '''
class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'completion_stage', 'assignee']
    template_name = 'task_manager_app/task_update.html'
    success_url = reverse_lazy('task-list') # This works but the others do not

''' Queries database to delete view '''
class TaskDeleteView(generic.DeleteView):
    model = Task
    fields = ['title', 'description', 'due_date', 'completion_stage', 'assignee']
    template_name = 'task_manager_app/task_delete.html'
    success_url = reverse_lazy('task-list')

''' Creates new view '''
class TaskCreateView(generic.CreateView):
    model = Task
    ''' Use form_class instead of fields to insure that due_date has a proper widget '''
    form_class = TaskForm
    template_name = 'task_manager_app/task_create.html'
    success_url = reverse_lazy('task-list')

###########################################################
#                   FUNCTION BASED MODELS                 #
###########################################################

''' HOME PAGE VIEW '''
def index(request):
    return render(request, 'task_manager_app/index.html')

#################################
#     TEAM ORIENTED METHODS     #
#################################

# Creates a team and sets user as team lead for team created
def createTeamPage(request):

    form = CreateTeamForm()

    if request.method == 'POST':
        form = CreateTeamForm(request.POST)
        if form.is_valid:
            team_name = form['team_name'].value()
            team_exists = Team.objects.filter(name=team_name).exists()
            
            if not team_exists:
                user = request.user
                user_name = request.user.username
                group = Group.objects.get(name='Team Lead')
                user.groups.add(group)

                # Create TeamLead object
                team_lead = TeamLead.objects.create(name=user_name, user=user)
                team_lead.save()

                # Create Team object
                team = Team.objects.create(name=team_name, lead=team_lead)
                team.save()

                messages.success(request, 'Successfully create team: ' + team_name)
                # Redirect to team page
                return redirect('index')
            else:
                error_message = "The team '{}' already exists. Please choose a different name.".format(team_name)
                return render(request, 'task_manager_app/create_team.html', {'form': form, 'error_message': error_message})

            
    context = {'form':form}
    return render(request, 'task_manager_app/create_team.html', context)

# Register a user to a team and give them a role
def joinTeamPage(request):

    form = JoinTeamForm()

    if request.method == 'POST':
        form = JoinTeamForm(request.POST)
        if form.is_valid:
            team_name = form['team_name'].value()
            team_exists = Team.objects.filter(name=team_name).exists()

            if team_exists:
                user = request.user
                user_name = request.user.username
                group = Group.objects.get(name='Team Member')
                user.groups.add(group)
            
                teamObj = Team.objects.get(name=team_name)
                team_member = TeamMember.objects.create(name=user_name, team=teamObj, user=user)
                team_member.save()

                messages.success(request, 'Successfully added to: ' + team_name)
                # Redirect to team page
                return redirect('index')
            else:
                error_message = "The team '{}' does not exist. Please try again.".format(team_name)
                return render(request, 'task_manager_app/join_team.html', {'form': form, 'error_message': error_message})

    context = {'form':form}
    return render(request, 'task_manager_app/join_team.html', context)

#################################
#       USER AUTHENTICATION     #
#################################

# Registers a user to the database
def registerPage(request):
    
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    
    context = {'form':form}
    return render(request, 'registration/register.html', context)
