from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
# from django.core.context_processors import csrf


def login(request):
    return render(request, 'account/login.html')

def register(request):
    return render(request, 'account/register.html')

def profile(request):
    return render(request, 'account/profile.html')

def edit_profile(request):
    return render(request, 'account/edit_profile.html')
