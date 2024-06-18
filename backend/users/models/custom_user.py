from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .user_manager import MyUserManager
from django.utils.translation import gettext_lazy as _
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField( verbose_name= _("email"), max_length=255, unique=True)
    is_superuser = models.BooleanField(verbose_name= _("is superuser?"), default=False)
    is_staff = models.BooleanField(verbose_name= _("is staff?"), default=False)
    is_active = models.BooleanField(verbose_name= _("is active?"), default=False)
    created_date = models.DateTimeField(verbose_name= _("created date"), auto_now_add=True)
    updated_date = models.DateTimeField(verbose_name= _("updated date"), auto_now=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = MyUserManager()
    
    def __str__(self):
        return self.email
    

