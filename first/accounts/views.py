from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('success')
    template_name = 'signup.html'


def success(request):
    response = render(request, 'success.html')
    return response
