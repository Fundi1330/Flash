from django.db import models
from .base import Base

class Post(Base):
    title = models.CharField(max_length=120)
    text = models.TextField()
    