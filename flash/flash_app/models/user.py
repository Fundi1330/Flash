from typing import Any, Optional
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class FlashUserManager(UserManager):
    def _create_user(self, email, password, **extra_fiels):
        if not email:
            raise ValueError('Email is not set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fiels)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, username: str, email: str | None = ..., password: str | None = ..., **extra_fields: Any) -> Any:
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email=email, password=password, extra_fiels=extra_fields)

class FlashUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(default='', unique=True)
    username = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=70)
    avatar = models.ImageField(upload_to='./images/avatars', default='./images/avatars/default.png')
    bio = models.CharField(max_length=150, default='')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = FlashUserManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f'<FlashUser {self.username}>'