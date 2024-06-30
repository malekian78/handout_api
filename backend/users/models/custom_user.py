from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager
from django_jalali.db import models as jmodels


class MyUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with (email, password)
        """
        if not email:
            raise ValueError("the Email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates a superuser with (email, password)
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name=_("email"), max_length=255, unique=True)
    is_superuser = models.BooleanField(verbose_name=_("is superuser?"), default=False)
    is_staff = models.BooleanField(verbose_name=_("is staff?"), default=False)
    is_active = models.BooleanField(verbose_name=_("is active?"), default=False)
    created_date = jmodels.jDateTimeField(
        verbose_name=_("created date"), auto_now_add=True
    )
    updated_date = jmodels.jDateTimeField(verbose_name=_("updated date"), auto_now=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = MyUserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.email
