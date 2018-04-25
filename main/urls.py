from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('get-advice-and-upload', views.get_advice_and_upload),
    path('upload-form', views.upload_form),
    path('faq', views.faq),
]