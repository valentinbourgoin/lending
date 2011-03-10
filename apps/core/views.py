# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from mongoengine.django.auth import User

from lending.apps.core.models import *
from lending.apps.books.models import *

def home(request):
    print request.user
    form = AuthenticationForm()
    books = Book.objects.all()
    return render_to_response(
        'core/home.html',
        {'books': books, 'form': form},
        context_instance=RequestContext(request))

def login(request):
    u = User(username=request.POST['username'])
    u.set_password(request.POST['password'])
    user = authenticate(username=u.username, password=u.password)
    
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/')
    return HttpResponseRedirect('/?bad')
