from rest_framework import serializers
from .models import Subscriber, EmailContent

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['email', 'subscribed']

class EmailContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailContent
        fields = ['title', 'body', 'created_at']