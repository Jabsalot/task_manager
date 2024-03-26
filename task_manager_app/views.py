from django.shortcuts import render
from django.http import HttpResponse

""" HOME PAGE VIEW """
def index(request):
    return render(request, 'task_manager_app/index.html')

""" LOGIN VIEWS """
def login(request):
    return HttpResponse('Login Page (NOT FINISHED)')

def logout(request):
    return HttpResponse('Logout Page (NOT FINISHED)')
