from django.shortcuts import render

# Create your views here.

def form_app(request):
  return render(request, 'form_app.html')