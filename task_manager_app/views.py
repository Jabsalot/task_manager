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
#       USER AUTHENTICATION     #
#################################

# Registers a user and gives them a role
def registerPage(request):
    
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid:
            user = form.save()
            username = form.cleaned_data.get('username')

            if 'teamLead':
                group = Group.objects.get(name='team_lead')
                user.groups.add(group)
                teamLead = TeamLead.objects.create(user=user)
                teamLead.save()
            else:
                group = Group.objects.get(name='team_member')
                user.groups.add(group)
                teamMember = TeamMember.objects.create(user=user)
                teamMember.save()

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    
    context = {'form':form}
    return render(request, 'registration/register.html', context)


