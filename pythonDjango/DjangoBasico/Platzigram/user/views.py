"""Users view"""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from user.models import Profile

def update_profile(request):
    """Update users profile"""
    return render(request, "users/update_profile.html")

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


def singup(request):
    """singup view"""
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']
        if passwd != passwd_confirmation:
            return render(request, 'users/singup.html', {'error':'Password confirmation does not match'})

        try:
            user = User.objects.create_user(username=username, password = passwd)
        except IntegrityError:
            return render(request, 'users/singup.html', {'error': 'Username is alredy in user'})
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request, 'users/singup.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
