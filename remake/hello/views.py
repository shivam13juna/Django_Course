from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.utils.html import escape
from django.urls import reverse


def index(request):
    return HttpResponse("Hello, you're at index of hello")


def session(request):
    request.session.set_test_cookie()
    request.session['user_id'] = 20
    return HttpResponse(request.session.items())
    # return HttpResponse(user)
    # if request.session.test_cookie_worked():
    #     return HttpResponse("Cookie can be set!")
    # else:
    #     return HttpResponse("Oh no, cookie can't be set!")
    # return HttpResponse(request.session.items())


def visit(request):
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    if request.session['num_visits'] > 5:
        request.session['num_visits'] = 0
    context = {'num_visits': num_visits}
    response = render(request, 'hello/visit.html', context=context)
    response.set_cookie('dj4e_cookie', '834a3bd2', max_age=1000)
    
    return response


def cookie(request):
    return HttpResponse(request.COOKIES.items())


def owner(request):
    return HttpResponse("Hello, world. 834a3bd2 is the polls index.")