from django.test import TestCase
from .forms import CreateTeamForm, JoinTeamForm, TaskForm

class TestForms(TestCase):

    ##########################################
    #               Create Team              #
    ##########################################

    def testCreateTeamFormValidData(self):
        form = CreateTeamForm(data={'team_name': 'Test Team'})
        self.assertTrue(form.is_valid())

    def testCreateTeamFormNoData(self):
        form = CreateTeamForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    ##########################################
    #                Join Team               #
    ##########################################

    def testJoinTeamFormValidData(self):
        form = JoinTeamForm(data={'team_name': 'Test Team'})
        self.assertTrue(form.is_valid())

    def testJoinTeamFormNoData(self):
        form = JoinTeamForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    ##########################################
    #                  Task                  #
    ##########################################

    def testTaskFormValidData(self):
        form = TaskForm(data={
            'title': 'Test Task',
            'description': 'Test Description',
            'due_date': '2024-04-24',
            'completion_stage': 'Not Started',
            'assignee': 1  # Assume a valid user is logged
        })
        self.assertTrue(form.is_valid())

    def testTaskFormNoData(self):
        form = TaskForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 5)  # 5 fields are required (email_sent not required)

    def testTaskFormInvalidDueDateFormat(self):
        form = TaskForm(data={
            'title': 'Test Task',
            'description': 'Test Description',
            'due_date': '24-04-2024',  # Invalid format
            'completion_stage': 'Not Started',
            'assignee': 1
        })
        self.assertFalse(form.is_valid())
        self.assertIn('due_date', form.errors)
