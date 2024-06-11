from django.contrib import admin

# Register your models here.
from .models import Subscriber, EmailContent

admin.site.register(Subscriber)
admin.site.register(EmailContent)