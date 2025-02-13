from django.shortcuts import render, redirect

def index(request):
    # Show the dashboard to authenticated users
    if request.user.is_authenticated:
        return redirect('/app/')

    # Show the landing page to everyone else
    return render(request, 'landing/index.html', {})