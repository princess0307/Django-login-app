from django.shortcuts import render
from django.shortcuts import render_to_response

from .models import Reg

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .form import RegForm
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('enter/index.html',c)


def cost(request):
    f= {}
    f.update(csrf(request))

    if request.method == 'POST':

        form = RegForm(request.POST)
        if form.is_valid():
            form.save()

            return render_to_response('enter/login.html',f)
    else:
        form = RegForm()
        return render_to_response('enter/login20.html')

    return render_to_response('enter/failure.html')


def auth_view(request):

    d= {}
    d.update(csrf(request))

    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        print username
        user = auth.authenticate(name=username, password=password)
        print user
        if user is not None:
                auth.login(request,user)

                return HttpResponseRedirect('enter/login1.html')

        else:

            return render_to_response('enter/login.html', d)
    return render_to_response('enter/failure.html',)


def loggedin(request):
    return render_to_response('enter/loggedin.html', {'name': request.user.name})


def logout(request):
    auth.logout(request)
    return render_to_response('enter/logout.html')