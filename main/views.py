from django.shortcuts import render
from main.forms import LegalDocForm, ClientForm
from main.models import Attorney, Client, Case

from main.utilities import find_attorney

# Create your views here.

def get_advice(request):
  if request.method == 'POST':
    # print(request.POST)
    legal_form = LegalDocForm(request.POST['pdf_file'])
    client_form = ClientForm(
      {
        'name': request.POST['name'],
        'county': request.POST['county'],
        'email': request.POST['email']
      }
    )

    if legal_form.is_valid() and client_form.is_valid():
      client_data = client_form.cleaned_data
      # Save client info

      atty = find_attorney()
      return redirect(request, 'success.html', {'attorney_name': attorney_info['name'], 'attorney_email': attorney_info['email']})

  else:
    legal_form = LegalDocForm()
    client_form = ClientForm()
    
  return render(request, 'form_app.html', {'legal_form': legal_form, 'client_form': client_form})