from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your models here.



class User(models.Model):
    title = models.CharField(max_length=100)


    def _str_(self):
        return self.title

