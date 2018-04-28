from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.http import FileResponse, HttpResponse


from main.forms import UploadLegalDoc, ClientForm
from main.models import Attorney, Client, Case, LegalDoc

from main.utilities import assign_attorney, email_form_to_attorney, gen_case_id

# Create your views here.

def home(request):
  return render(request, 'home.html')

def faq(request):
  return render(request, 'faq.html')



def upload_form(request):
  if request.method == 'POST':
    client_form = ClientForm(request.POST)
    legal_form = UploadLegalDoc(request.POST, request.FILES)

    # probably want to check each individually (for error msg) since `and` short circuits
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
      client_info = {
        'name': new_client.name,
        'email': new_client.email,
        'phone': new_client.phone
      }
      # email form and client info to attorney
      email_to_attorney = email_form_to_attorney(case_attorney.email, client_info, new_legal_doc.doc_uuid)

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

def doc_link_test(request):
  # doc_link = 'main/legaldocs/Axiom_UG_EN_anqIZyV.pdf'
  # return render(request, 'doc_link_test.html', {'doc_link': doc_link})
  file_data = FileResponse(open('main/legaldocs/Axiom_UG_EN_anqIZyV.pdf', 'rb'))
  response = HttpResponse(file_data, content_type='application/pdf')
  # response['Content-Disposition'] = 'attachment; filename="Axiom_UG_EN_anqIZyV.pdf"'
  return response

def document_link(request, doc_uuid):
  file_data = FileResponse(open('main/legaldocs/Axiom_UG_EN_anqIZyV.pdf', 'rb'))
  response = HttpResponse(file_data, content_type='application/pdf')

