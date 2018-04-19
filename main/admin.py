from django.contrib import admin

# Register your models here.

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Attorney, Client, Case, LegalDoc

admin.site.register(User, UserAdmin)

class AttorneyAdmin(admin.ModelAdmin):
  pass
admin.site.register(Attorney, AttorneyAdmin)

class ClientAdmin(admin.ModelAdmin):
  pass
admin.site.register(Client, ClientAdmin)

class CaseAdmin(admin.ModelAdmin):
  pass
admin.site.register(Case, CaseAdmin)

class LegalDocAdmin(admin.ModelAdmin):
  pass
admin.site.register(LegalDoc, LegalDocAdmin)

