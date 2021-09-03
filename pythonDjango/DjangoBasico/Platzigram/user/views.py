"""Users view"""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

def login_view(request):
    """Login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_log = authenticate(request, username=username, password=password)
    else:
        return render(request, 'users/login.html')

    if user_log:
        login(request, user_log)
        return redirect('feed')
    else:
        return render(request, 'users/login.html', {'error':'Invalid username or password'})
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')