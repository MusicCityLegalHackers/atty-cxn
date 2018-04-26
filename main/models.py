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
    on_delete=models.SET_NULL,
    null=True
  )
  attorney = models.ForeignKey(
    'Attorney',
    on_delete=models.SET_NULL,
    null=True
  )
  # category used to match Case with Attorney specialization
  category = models.CharField(max_length=30)
  opened_on = models.DateField(auto_now_add=True)
  closed_on = models.DateField(null=True)
  is_open = models.BooleanField(default=True)
  # case_id comes from `gen_case_id` in .utilities
  case_id = models.CharField(max_length=8)

  def __str__(self):
    return "Case {0}: {1}, {2}".format(str(self.case_id), str(self.client), str(self.attorney))

class LegalDoc(models.Model):
  name = models.CharField(max_length=100)
  date_submitted = models.DateField(auto_now_add=True)
  pdf_file = models.FileField(upload_to='main/legaldocs')
  client = models.ForeignKey(
    'Client',
    on_delete=models.SET_NULL,
    null=True
  )

  ## Need more descriptive str when Client doesn't exist
  def __str__(self):
    if self.name == '':
      doc_name = 'Untitled'
    return "{0}: {1}".format(str(self.client), doc_name)

