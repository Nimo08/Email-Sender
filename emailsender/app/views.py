from django.shortcuts import HttpResponse
from .tasks import send_bulk_emails_task


def send_bulk_emails_view(request):
    send_bulk_emails_task.delay()
    return HttpResponse("Bulk email sending has been initiated.")
    
