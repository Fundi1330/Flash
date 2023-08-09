from django.db import models
from ..models import FlashUser, Base

# Create your models here.


class Chat(Base):
    name = models.CharField(max_length=120)
    avatar = models.ImageField(upload_to='./media', default='/media/default.png')
    members = models.ManyToManyField(FlashUser, related_name='members')
    

class Message(Base):
    body = models.TextField()
    edited_at = models.DateTimeField(auto_now_add=True)
    replay_to = models.IntegerField(null=True)
    is_pinned = models.BooleanField(default=False)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)

