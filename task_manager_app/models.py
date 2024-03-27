from django.db import models

class TeamLead(models.Model):
    name = models.CharField(max_length=200)

# One-to-One (Team Lead)
# One-to-Many (Team Members)
class Team(models.Model):
    name = models.CharField(max_length=200)

    # One-to-Many Relationship
    lead = models.OneToOneField(TeamLead, on_delete=models.SET_NULL, null=True, related_name='teams')

class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.CASCASE, related_name='members')

# One-to-Many (Team Member)
class Task(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=200, blank=False)
    due_date = models.DateTimeField(blank=False)
    completion_stage = models.CharField(max_length=200, choices=[('Not Started', 'Not Started'),
                                                                 ('Working On', 'Working On'),
                                                                 ('Completed', 'Completed')], blank=True)

    ''' 
        One-to-Many Relationship 
        Each Task has a ForeignKey relationship with TeamMember 
        to represent the team member assigned to that task
    '''
    assignee = models.ForeignKey(TeamMember, on_delete=models.SET_NULL, null=False, related_name='tasks')



