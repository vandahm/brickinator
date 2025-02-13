from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

@login_required
def index(request):
    return render(request, 'user_profile/index.html', {})

@login_required
def edit(request):
    return render(request, 'user_profile/edit.html', {})

@login_required
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            login(request, request.user)
            return redirect('/app/profile/')
    else:
        form = PasswordChangeForm(user=request.user)


    return render(request, 'user_profile/password.html', {
        'form': form,
    })
