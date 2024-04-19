from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from .models import Task
from django.conf import settings

@shared_task()
def sendOverdueTaskEmails():
    print('TASKS BEING CHECKED FOR OVERDUE STATUS')

    # Get overdue tasks that haven't had an email notification
    overdue_tasks = Task.objects.filter(due_date__lt=timezone.now(), 
                                        completion_stage__in=['Not Started', 'Working On'],
                                        email_sent=False)
    
    for task in overdue_tasks:
        print("Running through tasks...")

        # Get the team lead's email associated with the task's assignee
        team_lead_email = task.assignee.team.lead.user.email

        print('EMAIL: ' + str(team_lead_email))

        # Send email to team lead
        subject = 'Task Overdue: {}'.format(task.title)
        message = 'The task "{}" assigned to {} is overdue. Task was due on {}'.format(task.title, task.assignee.name, task.due_date)
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [team_lead_email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        # Update email
        task.email_sent = True
        task.save()