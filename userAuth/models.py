from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.

# custom user model

class User(AbstractUser):
    role = models.CharField(max_length=10,blank=False,null=False)

def foo():
    return ''

def foofoo():
    return 'active'

# mentor model
class Mentor(models.Model):
    mentorid = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100, default='')
    designation = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    status = models.CharField(max_length=10, default='active')
    phone = models.CharField(max_length=10, null=True, blank=True, unique=True, validators=[MinLengthValidator(10)])
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    class Meta:
        db_table = 'mentors'

# intern model

class Intern(models.Model):
    internid = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    mentorid = models.ForeignKey(Mentor, on_delete=models.DO_NOTHING)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=100, default='NA')
    phone = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(10)])
    college = models.CharField(max_length=255)
    status = models.CharField(max_length=10, default='active')
    doj = models.DateField(null=False,blank=False)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    class Meta:
        db_table = 'interns'