# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http.response import *
from .models import *
from django.contrib.auth.models import User

# Create your views here.
@login_required
def dashboard(request):
    trans = transaction.objects.filter(user=User.objects.get_by_natural_key(request.user.username))
    return render(request, 'table.html', {'trans':trans})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            return HttpResponseRedirect('/login/')
        return HttpResponseRedirect('/dashboard/')
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')
