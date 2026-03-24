from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import timezone
from apps.core.models import BaseModel


class CustomUserManager(BaseUserManager):

    def create_user(self, password=None, **extra_fields):
        user=self.model(**extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        Category.objects.create(created_by=user)
        return user
    
    def create_superuser(self):
        pass

class CustomUser(BaseModel, AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    national_id = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()
