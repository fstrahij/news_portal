from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	hello = '<h1>hello word</h1>'
	return HttpResponse(hello)
# Create your views here.
