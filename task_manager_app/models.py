from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

''' Team Lead Model '''
class TeamLead(models.Model):
    name = models.CharField(max_length=200)

    # Relational 
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

''' Team Model '''
class Team(models.Model):
    name = models.CharField(max_length=200)
    
    # Relational 
    lead = models.OneToOneField(TeamLead, on_delete=models.SET_NULL, null=True, related_name='teams')

    def __str__(self):
        return self.name

''' Team Member Model '''
class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    
    # Relational 
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
''' Task Model '''
class Task(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=200, blank=False)
    due_date = models.DateField(blank=False)
    completion_stage = models.CharField(max_length=200, choices=[('Not Started', 'Not Started'),
                                                                 ('Working On', 'Working On'),
                                                                 ('Completed', 'Completed')], blank=True)
    email_sent = models.BooleanField(blank=True, default=False)
    ''' 
        One-to-Many Relationship 
        Each Task has a ForeignKey relationship with TeamMember 
        to represent the team member assigned to that task
    '''
    assignee = models.ForeignKey(TeamMember, on_delete=models.SET_NULL, null=True, related_name='tasks')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('task-detail', args=[str(self.id)]) 