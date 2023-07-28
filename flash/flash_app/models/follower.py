from django.db import models
from .user import FlashUser

class Follower(models.Model):
    user = models.ForeignKey(FlashUser, on_delete=models.CASCADE, name='user', related_name='user')
    follower = models.ForeignKey(FlashUser, on_delete=models.CASCADE, name='follower', related_name='follower')