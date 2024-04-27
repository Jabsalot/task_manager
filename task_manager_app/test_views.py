from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from .models import Team, TeamMember

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.team_lead_group = Group.objects.create(name='Team Lead')
        self.team_member_group = Group.objects.create(name='Team Member')

    ##########################################
    #               Create Task              #
    ##########################################

    def test_create_task(self):
        # Creates a team
        team = Team.objects.create(name='Test Team')

        # Creates a team member
        team_member = TeamMember.objects.create(name='Test Team Member', team=team, user=self.user)

        self.client.force_login(self.user)
        response = self.client.post(reverse('task-create-page', kwargs={'team_member_id': team_member.id}), {'title': 'Test Task', 
                                                                                                             'description': 'Test Description',
                                                                                                             'due_date': '2024-4-24',
                                                                                                             'completion_stage': 'Not Started',
                                                                                                             'assignee': team_member.id})

        self.assertEqual(response.status_code, 302)  # Check if the view redirects after creating a task
        self.assertEqual(response.url, reverse('team-member-tasks', kwargs={'team_member_id': team_member.id}))  # Check if the redirection is to the correct URL

    ##########################################
    #               Create Team              #
    ##########################################

    def test_create_team_page(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('create-team-page'), {'team_name': 'Test Team'})

        self.assertEqual(response.status_code, 302)  # Check if the view redirects after creating a team
        self.assertEqual(response.url, reverse('index'))  # Check if the redirection is to the correct URL
        self.assertTrue(Team.objects.filter(name='Test Team').exists())  # Check if the team is created in the database

    ##########################################
    #                Join Team               #
    ##########################################

    def test_join_team_page(self):
        team = Team.objects.create(name='Test Team')
        
        self.client.force_login(self.user)
        response = self.client.post(reverse('join-team-page'), {'team_name': 'Test Team'})

        self.assertEqual(response.status_code, 302)  # Check if the view redirects after joining a team
        self.assertEqual(response.url, reverse('index'))  # Check if the redirection is to the correct URL
        self.assertTrue(TeamMember.objects.filter(name=self.user.username, team=team).exists())  # Check if the team member is created in the database

