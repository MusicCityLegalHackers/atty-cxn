from django.shortcuts import render, redirect
from main.forms import UploadLegalDoc, ClientForm
from main.models import Attorney, Client, Case, LegalDoc

from main.utilities import find_attorney

# Create your views here.

def home(request):
  return render(request, 'home.html')

def upload(request):
  if request.method == 'POST':
    legal_form = UploadLegalDoc(request.POST)
    if legal_form.is_valid():
      # save doc
      return redirect('/main/get-advice')
    else:
      return redirect('/main/get-advice')

  else:
    legal_form = UploadLegalDoc()
    return render(request, 'upload.html', {'legal_form': legal_form})

def get_advice(request):
  if request.method == 'POST':
    # print(request.POST)
    # legal_form = UploadLegalDoc(request.POST['pdf_file'])
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

def get_advice_and_upload(request):
  if request.method == 'POST':
    # client_form = ClientForm(
    #   {
    #     'name': request.POST['name'],
    #     'county': request.POST['county'],
    #     'email': request.POST['email']
    #   }
    # )
    client_form = ClientForm(request.POST)
    legal_form = UploadLegalDoc(request.POST, request.FILES)
    # probably want to check each individually since `and` short circuits
    if legal_form.is_valid() and client_form.is_valid():
      # save to db
      client_form_data = client_form.cleaned_data
      new_client = Client.objects.create(
        name=client_form_data['name'],
        county=client_form_data['county'],
        email=client_form_data['email']
      )
      new_legal_doc = LegalDoc.objects.create(
        pdf_file=request.FILES['pdf_file'],
        client=new_client
      )
  else:
    client_form = ClientForm()
    legal_form = UploadLegalDoc()
  return render(request, 'get_advice_and_upload.html', {'client_form': client_form, 'legal_form': legal_form})

