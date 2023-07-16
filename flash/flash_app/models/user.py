from django.contrib.auth.models import AbstractUser
from django.db import models

class FlashUser(AbstractUser):
    full_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='./')