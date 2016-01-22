from django.shortcuts import render
from django.http.response import HttpResponse
import django

# Create your views here.
def homepage(req):
    return HttpResponse("Hello, django! version: " + str(django.VERSION))