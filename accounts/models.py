from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import datetime
# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='media/accounts/profile',
                              default='media/accounts/profile/default.jpg')
    
    description = models.TextField(blank=True)
         

class Message(models.Model):
    pub_date = models.DateTimeField(default=timezone.now)
    post = models.TextField()
    post_to = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='post_to')
    post_by = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='post_by')
    
    class Meta:
        ordering = ['-pub_date']
    
    
    def get_replies(self):
        result = Reply.objects.filter(message_id=self.id)
        return result
    
    
class Reply(models.Model):
    pub_date = models.DateTimeField(default=timezone.now)
    reply = models.TextField()
    reply_by = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                related_name='reply_by')
    message = models.ForeignKey(Message,
                                on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['pub_date']