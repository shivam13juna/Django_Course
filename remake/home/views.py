from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.utils.html import escape
from django.urls import reverse


def session(request):
    return HttpResponse(request.session.items())
    

def owner(request):
    return HttpResponse("Hello, world. 834a3bd2 is the polls index.")