from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from .managers import CustomUserManager


class User(AbstractBaseUser):
    user_id = models.CharField(max_length=100, unique=True, null=True)
    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "user_id"
    REQUIRED_FIELDS = ["name","email"]

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser