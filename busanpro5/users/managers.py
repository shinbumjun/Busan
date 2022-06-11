from django.contrib.auth.base_user import BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, user_id, email, name, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """
        if not user_id:
            raise ValueError("The given name must be set")
        if not email:
            raise ValueError("The given name must be set")

        email = self.normalize_email(email)
        user = self.model(user_id=user_id, email=email, name=name, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, user_id, email, name, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(user_id, email, name, password, **extra_fields)

    def create_superuser(self, user_id, email, name, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(user_id, email, name, password, **extra_fields)