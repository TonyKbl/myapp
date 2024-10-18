from django.db import models

from django.contrib.auth.models import User
from messaging.models import Message

# Create your models here.
class Report(models.Model):
    def custom_user():
        return User.objects.get(username='admin')
    
    user = models.ForeignKey(User, on_delete=models.SET(custom_user), related_name='reporter')
    time = models.DateTimeField(auto_now_add=True)
    reason = models.TextField(null=True, blank=False)

class ReportedPhoto(Report):
    image_url = models.CharField(max_length=500)

class ReportedMessage(Report):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='reported_message')
    msg_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_to')
    msg_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_from')

class ReportedPage(Report):
    pass

class ReportedProfile(Report):
    profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_profile')

    def __str__(self):
        return self.profile.username

    

