from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.utils import timezone
from .models import Task
from django.conf import settings

@receiver(post_save, sender=Task)
def taskOverdueNotification(sender, instance, created, **kwargs):

    if (instance.completion_stage == 'Not Started' or instance.completion_stage == 'Working On') and instance.due_date < timezone.now().date():
        # Get the team lead's email associated with the task's assignee
        team_lead_email = instance.assignee.team.lead.user.email

        # Send email to team lead
        subject = 'Task Overdue: {}'.format(instance.title)
        message = 'The task "{}" assigned to {} is overdue'.format(instance.title, instance.assignee.name)
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [team_lead_email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
