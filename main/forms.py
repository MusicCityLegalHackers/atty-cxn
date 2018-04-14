from django.forms import ModelForm
from main.models import LegalDoc, Client

class LegalDocForm(ModelForm):
  class Meta:
    model = LegalDoc
    fields = ['pdf_file']

class ClientForm(ModelForm):
  class Meta:
    model = Client
    exclude = []