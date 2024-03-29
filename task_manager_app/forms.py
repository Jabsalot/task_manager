from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# What is a form forms?
""" 
    The form class specifies the fields in the form, their layout, display wdigets,
    labels, initial values, valid values, and (once validated) the error messages 
    associated with invalid fields. The class also provides methods for rendering 
    itself in templates using predefined formated (tables, lists, etc.) or for 
    getting the value of any element (enabling fine-grained manual rendering)
"""

# What are they used for?
#   - Forms are used for taking input from the user in some manner
#     and using that informating for logical operations on databases.

# How do they work with HTML?
#   - Django maps fields defined in Django forms into HTML input fields.
#   - Django handles three distinct parts of the work involved in forms:
#       1. Preparing and restructuing data to make it ready for rendering
#       2. Creating HTML forms for the data
#       3. Receiving and processing submitted forms and data from the client

class TaskForm(ModelForm):
    due_date = forms.DateField(input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'completion_stage', 'assignee']
        template_name = 'task_update.html'
