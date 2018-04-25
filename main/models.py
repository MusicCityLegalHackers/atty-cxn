from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

from itertools import cycle

class User(AbstractUser):
  pass

class Attorney(models.Model):
  name = models.CharField(max_length=50)
  county = models.CharField(max_length=50)
  state = models.CharField(max_length=50)
  email = models.CharField(max_length=50, unique=True)
  phone = models.CharField(max_length=12, unique=True)
  specialization = models.CharField(max_length=50)
  bpr = models.IntegerField() # Bar ID
  is_next = models.BooleanField(default=False)

  def __str__(self):
    return self.name + " (Attorney)"

class Client(models.Model):
  name = models.CharField(max_length=50)
  county = models.CharField(max_length=50)
  state = models.CharField(max_length=50)
  email = models.CharField(max_length=50, unique=True)
  phone = models.CharField(max_length=12, unique=True)

  def __str__(self):
    return self.name + " (Client)"

class Case(models.Model):
  client = models.ForeignKey(
    'Client',
    on_delete=models.PROTECT,
  )
  attorney = models.ForeignKey(
    'Attorney',
    on_delete=models.PROTECT,
  )
  # category used to match Case with Attorney specialization
  category = models.CharField(max_length=30)
  opened_on = models.DateField(auto_now_add=True)
  closed_on = models.DateField()
  is_open = models.BooleanField(default=True)
  # case_id comes from `gen_case_id` in .utilities
  case_id = models.CharField(max_length=8)

  def __str__(self):
    return "Case {0}: {1} (Client), {2} (Attorney)".format(str(case_id), str(self.client), str(self.attorney))

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

