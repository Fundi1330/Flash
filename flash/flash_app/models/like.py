from django.db import models
from .base import Base
from . import Post

class Like(Base):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')