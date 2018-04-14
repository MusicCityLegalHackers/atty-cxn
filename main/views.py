from django.shortcuts import render, redirect
from main.forms import LegalDocForm, ClientForm
from main.models import Attorney, Client, Case

from main.utilities import find_attorney

# Create your views here.

def home(request):
  return render(request, 'home.html')

def upload(request):
  if request.method == 'POST':
    legal_form = LegalDocForm(request.POST)
    if legal_form.is_valid():
      # save doc
      return redirect('/main/get-advice')
    else:
      return redirect('/main/get-advice')

  else:
    legal_form = LegalDocForm()
    return render(request, 'upload.html', {'legal_form': legal_form})

def get_advice(request):
  if request.method == 'POST':
    # print(request.POST)
    # legal_form = LegalDocForm(request.POST['pdf_file'])
    client_form = ClientForm(
      {
        'name': request.POST['name'],
        'county': request.POST['county'],
        'email': request.POST['email']
      }
    )

    if client_form.is_valid():
      client_data = client_form.cleaned_data
      # Save client info

      atty = find_attorney()
      return render(request, 'success.html', {'attorney_name': atty.name, 'attorney_email': atty.email})

  else:
    client_form = ClientForm()
    
  return render(request, 'get_advice.html', {'client_form': client_form})

