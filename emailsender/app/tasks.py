from celery import shared_task
from django.core.mail import send_mail
from .models import Subscriber, EmailContent

@shared_task
def send_email_task(email, subject, message):
    """
    Task to send an email using Django's send_mail function.
    """
    send_mail(
        subject,
        message,
        'host.user.api@gmail.com',
        [email],
        fail_silently=False,
    )

@shared_task
def send_bulk_emails_task():
    """
    Task to send bulk emails to all subscribed subscribers.
    """
    subscribers = Subscriber.objects.filter(subscribed=True)
    email_content = EmailContent.objects.last()  # Assuming you want to send the latest email content

    for subscriber in subscribers:
        send_email_task.delay(subscriber.email, email_content.title, email_content.body)
