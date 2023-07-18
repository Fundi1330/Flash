from django.db import models
from .base import Base
from .comment import Comment
from .like import Like

class Post(Base):
    title = models.CharField(max_length=120)
    text = models.TextField(max_length=2500)
    likes = models.ManyToManyField(Like)
    images = models.ImageField('./', default='./images/posts/default.png')
    comments = models.ManyToManyField(Comment)