from rest_framework import serializers
from .models import User, Message, Reply

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        user = User
        message = Message
        reply = Reply
        fields = '__all__'
    