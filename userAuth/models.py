from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# custom user model

class User(AbstractUser):
    collabid = models.CharField(max_length=10,unique=True,null=False,blank=False)
    role = models.CharField(max_length=10,blank=False,null=False)

