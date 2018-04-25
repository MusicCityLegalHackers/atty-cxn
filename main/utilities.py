from .models import Attorney
from django.utils.crypto import get_random_string

def assign_attorney(state, county, specialization):
  '''
    Start with a query for attorneys in Client's state & county and then proceed to get the 
    'next' in that subset.
    This way means that in the entire table there will be several attorneys labeled 'next' - 
    in particular, there will be exactly as many as there are counties.
    This shouldn't be a problem as long as we always start with the above query and then proceed 
    to find and increment the 'next'.
  '''
  area_attorneys = Attorney.objects.filter(state=state, county=county, specialization=specialization)
  next_atty = area_attorneys.get(is_next=True)
  next_atty.is_next = False
  # increment
  next_pk = next_atty.pk + 1
  new_next = None
  while not new_next:
    try:
      new_next = area_attorneys.get(pk=next_pk)
      next_next.is_next = True
    except:
      next_pk += 1
  return next_atty

def gen_case_id(length=8):
  '''
    Returns uppercase random string of length `length`
  '''
  return get_random_string(length).upper()
