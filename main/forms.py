from django import forms
from main.models import LegalDoc, Client

class ClientForm(forms.ModelForm):
  class Meta:
    model = Client
    exclude = []

class UploadLegalDoc(forms.ModelForm):
  class Meta:
    model = LegalDoc
    fields = ['pdf_file']

# class UploadLegalDoc(forms.Form):
#     # title = forms.CharField(max_length=50)
#     pdf_file = forms.FileField()

