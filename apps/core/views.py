# -*- coding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm

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
