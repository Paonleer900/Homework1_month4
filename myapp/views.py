from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def text_response(request):
    return HttpResponse("Hello! This is a simple text response.")

def html_response(request):
    return render(request, 'myapp/hello.html')
