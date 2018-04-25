from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.home),
    path('upload-form', views.upload_form),
    path('faq', views.faq),
    path('case', views.case_lookup),
    re_path('case/(?P<case_id>[0-9A-Z]{8})/$', views.case_lookup),
]
