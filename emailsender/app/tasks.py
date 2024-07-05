from celery import shared_task
from django.core.mail import send_mail
from .models import Subscriber, EmailContent
from django.conf import settings

@shared_task
def send_email_task(email, subject, message):
    """
    Task to send an email using Django's send_mail function.
    """
    try:
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
    except Exception as e:
        # Log the error
        print(f"Failed to send email to {email}: {str(e)}")
    
@shared_task
def send_bulk_emails_task():
    """
    Task to send bulk emails to all subscribed subscribers.
    """
    subscribers = Subscriber.objects.filter(subscribed=True)
    email_content = EmailContent.objects.last()  # Assuming you want to send the latest email content

    for subscriber in subscribers:
        send_email_task.delay(subscriber.email, email_content.title, email_content.body)
