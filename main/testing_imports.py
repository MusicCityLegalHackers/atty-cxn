from main.models import LegalDoc, Case, Client, Attorney

from main.utilities import email_form_to_attorney

from django.conf import settings

ld = LegalDoc.objects.get(doc_uuid='e171400b-02a5-43f8-8c1c-0c2f1cf59c30')

client_info = {
  'name': 'Paul Johnson',
  'email': 'paul@pjohnson.com',
  'phone': '283-485-8683'
}

atty_email = 'lawsonpd@gmail.com'
