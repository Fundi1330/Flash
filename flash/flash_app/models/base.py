from django.db import models
from .user import FlashUser

class Base(models.Model):
    create_date = models.DateTimeField(auto_now=True)
    edit_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(FlashUser, on_delete=models.CASCADE)

    class Meta:
        abstract = True