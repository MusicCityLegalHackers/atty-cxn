from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  pass

class Attorney(models.Model):
  name = models.CharField(max_length=50)
  county = models.CharField(max_length=50)

class LegalForm(models.Model):
  pass