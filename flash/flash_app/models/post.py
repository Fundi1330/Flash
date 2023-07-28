from django.db import models
from .base import Base
from .comment import Comment

class Post(Base):
    title = models.CharField(max_length=120)
    text = models.TextField(max_length=2500)
    images = models.ImageField('./', default='./images/posts/default.png')
    comments = models.ManyToManyField(Comment)