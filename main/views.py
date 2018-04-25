from django.shortcuts import render, redirect
from main.forms import UploadLegalDoc, ClientForm
from main.models import Attorney, Client, Case, LegalDoc

from main.utilities import assign_attorney, gen_case_id

# Create your views here.

def home(request):
  return render(request, 'home.html')

def get_advice_and_upload(request):
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

def upload_form(request):
  if request.method == 'POST':
    client_form = ClientForm(request.POST)
    legal_form = UploadLegalDoc(request.POST, request.FILES)

    # probably want to check each individually since `and` short circuits
    if legal_form.is_valid() and client_form.is_valid():
      client_form_data = client_form.cleaned_data
      # save Client to db
      ## Should see whether client is in db already
      new_client = Client.objects.create(
        name=client_form_data['name'],
        county=client_form_data['county'],
        state=client_form_data['state'],
        email=client_form_data['email']
      )
      # save LegalDoc to db
      new_legal_doc = LegalDoc.objects.create(
        pdf_file=request.FILES['pdf_file'],
        client=new_client
      )
      case_category = request.POST['category']
      # get next attorney
      case_attorney = assign_attorney(new_client.state, new_client.county, case_category)
      # create Case
      new_case = Case.objects.create(
        client=new_client,
        attorney=case_attorney,
        ## Should make sure case_id doesn't already exist in db
        case_id=gen_case_id()
      )
      ## may want to set num_days somewhere else
      num_days = 2
      return render(
        request,
        'upload_successful.html',
        {'num_days': num_days, 'case_id': new_case.case_id}
      )
  else:
    client_form = ClientForm()
    legal_form = UploadLegalDoc()
  return render(request, 'upload_form.html', {'client_form': client_form, 'legal_form': legal_form})

def faq(request):
  return render(request, 'faq.html')

def case_lookup(request, case_id):
  return render(request, 'case.html', {'case_id': case_id})
