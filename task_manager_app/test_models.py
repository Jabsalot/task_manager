from django.test import TestCase

from django.contrib.auth.models import User
from task_manager_app.models import Task, TeamMember, TeamLead, Team

from datetime import datetime

class ModelTestClass(TestCase):

    ###############################
    # Populate and create objects #
    ###############################

    def setUp(self):

        self.teamLead = TeamLead.objects.create(
            name="Test Team Lead",
        )

        self.team = Team.objects.create(
            name = "Test Team",
            lead = self.teamLead,
        )

        self.teamMember = TeamMember.objects.create(
            name = "Test Team Member",
            team = self.team,
        )

        due_date = datetime(2024, 4, 30)
        self.task = Task.objects.create(
            title = "Test Task",
            description = "Test description",
            due_date = due_date,
            completion_stage = "Not Started",
            email_sent = False,
            assignee = self.teamMember,
        )

    ###############
    # Test Object #
    ###############

    def test_teamLead_creation(self):
        self.assertEqual(self.teamLead.name, 'Test Team Lead')

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.lead, self.teamLead)

    def test_teamMember_creation(self):
        self.assertEqual(self.teamMember.name, 'Test Team Member')
        self.assertEqual(self.teamMember.team, self.team)

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'Test description')
        self.assertEqual(self.task.due_date.year, 2024)
        self.assertEqual(self.task.due_date.month, 4)
        self.assertEqual(self.task.due_date.day, 30)
        self.assertEqual(self.task.completion_stage, 'Not Started')
        self.assertFalse(self.task.email_sent) # Check is email_sent is False
        self.assertEqual(self.task.assignee, self.teamMember)