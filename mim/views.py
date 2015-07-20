from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf


def login(request):
    csrf_dict = {}
    csrf_dict.update(csrf(request))
    return render_to_response('login_and_register.html', csrf_dict)


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
    return render_to_response()


def index(request):
    return render_to_response('index.html', {'username': request.user.username})


def products(request):
    return render_to_response('products.html')


def customers(request):
    return render_to_response('customers.html')


def logout(request):
    csrf_dict = {}
    csrf_dict.update(csrf(request))
    auth.logout(request)
    return render_to_response('login_and_register.html', csrf_dict)
