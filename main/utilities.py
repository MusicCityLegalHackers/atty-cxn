from main.models import Attorney

def find_attorney():
  atty = Attorney.objects.get(pk=1)
  return atty