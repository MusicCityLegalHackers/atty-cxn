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
  bpr = models.IntegerField() # Bar ID

  def __str__(self):
    return self.name + " Attorney"

class Client(models.Model):
  name = models.CharField(max_length=50)
  county = models.CharField(max_length=50)
  email = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Case(models.Model):
  client = models.ForeignKey(
    'Client',
    on_delete=models.PROTECT,
  )
  attorney = models.ForeignKey(
    'Attorney',
    on_delete=models.PROTECT,
  )

  def __str__(self):
    return "Case: {0} (Client), {1} (Attorney)".format(str(self.client), str(self.attorney))

class LegalDoc(models.Model):
  name = models.CharField(max_length=100)
  date_submitted = models.DateField(auto_now_add=True)
  pdf_file = models.FileField(upload_to='main/legaldocs')
  client = models.ForeignKey(
    'Client',
    on_delete=models.PROTECT,
  )

  def __str__(self):
    return "{0} ({1})".format(self.name, str(self.client))

