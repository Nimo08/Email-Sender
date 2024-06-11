from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed = models.BooleanField(default=True)

class EmailContent(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    