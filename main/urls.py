from django.urls import path

from . import views

urlpatterns = [
    path('iframe-test/', views.iframe_test),
]