from django.shortcuts import render
from main.forms import LegalDocForm, ClientForm

# Create your views here.

def get_advice(request):
  if request.method == 'POST':
    pass
  if request.method == 'GET':
    legal_form = LegalDocForm()
    client_form = ClientForm()
    return render(request, 'form_app.html', {'legal_form': legal_form, 'client_form': client_form})