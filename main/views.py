from django.shortcuts import render, redirect
from django.urls import reverse
from main.forms import UploadLegalDoc, ClientForm
from main.models import Attorney, Client, Case, LegalDoc

from main.utilities import assign_attorney, gen_case_id

# Create your views here.

def home(request):
  return render(request, 'home.html')

def faq(request):
  return render(request, 'faq.html')



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
        email=client_form_data['email'],
        phone=client_form_data['phone']
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

def case_lookup(request):
  if request.method == 'POST':
    url = reverse('case-details', kwargs={'case_id': request.POST['case-id']})
    return redirect(url)
  else:
    return render(request, 'case_lookup.html')

def case_details(request, case_id=None):
  if request.method == 'GET':
    c = Case.objects.get(case_id=case_id)
    return render(
      request,
      'case.html',
      {
        'opened_on': c.opened_on,
        'attorney': c.attorney.name,
        'case_id': c.case_id,
        'is_open': c.is_open,
        'closed_on': c.closed_on
      }
    )
  else:
    url = reverse('case-lookup')
    return redirect(url)
