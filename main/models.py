from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  pass

class Attorney(models.Model):
  name = models.CharField(max_length=50)
  county = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  specialization = models.CharField(max_length=50)
  bpr = models.IntegerField()

class Client(models.Model):
  name = models.CharField(max_length=50)
  county = models.CharField(max_length=50)
  email = models.CharField(max_length=50)

class Case(models.Model):
  client = models.ForeignKey(
    'Client',
    on_delete=models.PROTECT,
  )
  attorney = models.ForeignKey(
    'Attorney',
    on_delete=models.PROTECT,
  )

class LegalForm(models.Model):
  pdf_file = models.FileField(upload_to='legalforms')