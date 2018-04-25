from .models import Attorney
from django.utils.crypto import get_random_string

def find_attorney():
  atty = Attorney.objects.get(pk=1)
  return atty

def gen_case_id(length=8):
  '''
    Returns uppercase random string of length `length`
  '''
  return get_random_string(length).upper()

