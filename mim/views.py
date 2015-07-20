from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

def login(request):
    csrf_dict = {}
    csrf_dict.update(csrf(request))
    return render_to_response('login.html', csrf_dict)


def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/mim/index/')
    else:
        return HttpResponseRedirect('/mim/invalid/')


def invalid_login(request):
    if request.user.is_anonymous():
        return HttpResponseRedirect('/mim/login')


def index(request):
    csrf_dict = {}
    csrf_dict.update(csrf(request))
    if request.user.is_active and request.user and request.user.is_staff or request.user.is_superuser:
        return render_to_response('index.html', {'username': request.user.username})
    else:
        csrf_dict.update({'errors': ['You are not an authorised user.']})
        return render_to_response('login.html', csrf_dict)


def products(request):
    csrf_dict = {}
    csrf_dict.update(csrf(request))
    if request.user.is_active and request.user and request.user.is_staff or request.user.is_superuser:
        return render_to_response('products.html')
    else:
        csrf_dict.update({'errors': ['You are not an authorised user.']})
        return render_to_response('login.html', csrf_dict)

def customers(request):
    csrf_dict = {}
    csrf_dict.update(csrf(request))
    if request.user.is_active and request.user and request.user.is_staff or request.user.is_superuser:
        return render_to_response('customers.html')
    else:
        csrf_dict.update({'errors': ['You are not an authorised user.']})
        return render_to_response('login.html', csrf_dict)


def transactions(request):
    csrf_dict = {}
    csrf_dict.update(csrf(request))
    if request.user.is_active and request.user and request.user.is_staff or request.user.is_superuser:
        return render_to_response('transactions.html')
    else:
        csrf_dict.update({'errors': ['You are not an authorised user.']})
        return render_to_response('login.html', csrf_dict)


def logout(request):
    csrf_dict = {}
    csrf_dict.update(csrf(request))
    auth.logout(request)
    return render_to_response('login.html', csrf_dict)
