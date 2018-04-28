from .models import Attorney
from django.utils.crypto import get_random_string

from django.conf import settings
from django.core.mail import send_mail, EmailMessage

def assign_attorney(state, county, specialization):
  '''
    Start with a query for attorneys in Client's state & county and then proceed to get the 
    'next' in that subset.
    This way means that in the entire table there will be several attorneys labeled 'next' - 
    in particular, there will be (approx.) n=counties*specializations many.
    This shouldn't be a problem as long as we always start with the above query and then proceed 
    to find and increment the 'next'.
  '''
  attorneys_subset = Attorney.objects.filter(state=state, county=county, specialization=specialization)
  next_atty = attorneys_subset.get(is_next=True)
  next_atty.is_next = False
  next_atty.save()
  # increment
  next_pk = next_atty.pk + 1
  new_next = None
  while not new_next:
    try:
      new_next = attorneys_subset.get(pk=next_pk)
      new_next.is_next = True
      new_next.save()
    except:
      next_pk += 1
  return next_atty

## Not necessary
# def get_doc_link(document):
#   file_data = FileResponse(open('main/legaldocs/Axiom_UG_EN_anqIZyV.pdf', 'rb'))
#   response = HttpResponse(file_data, content_type='application/pdf')

def email_form_to_attorney(atty_email, client_info, legal_doc):
  '''
    atty_email -> str
    client_info -> dict
    legal_doc -> db object
  '''
  # In production this would be properly formatted for an abosulute URL (e.g. 'https://...')
  doc_link = 'case/document/{0}'.format(legal_doc.doc_uuid)

  # subject, from_email, to = 'New document to review from AttorneyCxn', 'attorneycxn@gmail.com', atty_email
  message_body = 'Someone needs a document reviewed! \n \
             Here are the client\'s details: \n \
             Name: {0} \n \
             Email: {1} \n \
             Phone number: {2} \n \
             The form to review is included as an attachment (PDF). \n \
             You can also view or download the form here: {3} \n \
             \n \
             Your help is greatly appreciated!'.format(client_info['name'], client_info['email'], client_info['phone'], doc_link)

  email_msg = EmailMessage(
    'New document to review from AttorneyCxn', # Subject
    message_body, # Message body
    'attorneycxn@gmail.com', # From
    [atty_email], # To
  )

  email_msg.attach_file(legal_doc.pdf_file.name, 'application/pdf')
  email_msg.send(
    fail_silently=False
  )

  return 1

def gen_case_id(length=8):
  '''
    Returns uppercase random string of length `length`
  '''
  return get_random_string(length).upper()
