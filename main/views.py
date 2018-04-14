from django.shortcuts import render

# Create your views here.

def iframe_test(request):
  return render(request, 'iframe_test.html')