from django.db import models
from .base import Base

class Comment(Base):
    text = models.TextField(max_length=800)