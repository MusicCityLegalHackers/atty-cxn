from django.urls import path

from . import views

urlpatterns = [
    path('get-advice', views.get_advice),
]