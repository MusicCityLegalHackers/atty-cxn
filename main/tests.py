from django.test import TestCase

from main.models import LegalDoc, Attorney, Case, Client
from main.utilities import email_form_to_attorney, gen_case_id

# Create your tests here.

class SendEmailTestCase(TestCase):
  def setUp(self):

    # ATTORNEY data
    atty_email = 'lawsonpd@gmail.com'
    new_atty = Attorney.objects.create(
      name='Peter Lawson',
      email=atty_email,
      county='Davidson',
      state='TN',
      phone='767-272-7737',
      bpr='2323',
      specialization='Tort'
    )

    # CLIENT data
    new_client = Client.objects.create(
      name='Jane Simpson',
      county='Davidson',
      state='TN',
      email='jane@jsimpson.com',
      phone='525-236-7567'
    )
    client_info = {
      'name': new_client.name,
      'email': new_client.email,
      'phone': new_client.phone
    }

    # CASE data
    new_case = Case.objects.create(
      client=new_client,
      attorney=new_atty,
      case_id=gen_case_id()
    )

    # DOC data
    pdf = open('main/legaldocs/Axiom_UG_EN.pdf', 'r')

    ## Saving the file isn't working here. Test is failing.
    doc = LegalDoc.objects.create(
      name='my doc',
      pdf_file=pdf.read(),
      client=new_client,
      case=new_case
    )

  def test_send_email(self):
    self.assertEqual(email_form_to_attorney(atty_email, client_info, doc), 1)
