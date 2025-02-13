from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def index(request):
    redirect('/')

@login_required
def signout(request):
    logout(request)
    return redirect('/')



