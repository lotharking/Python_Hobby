"""Users view"""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

# Forms
from user.forms import ProfileForm, SignupForm

@login_required
def update_profile(request):
    """Update users profile"""
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()
            return redirect('update_profile')
    else:
        form = ProfileForm()

    return render(
        request=request, 
        template_name="users/update_profile.html",
        context={
            'profile':profile,
            'user':request.user,
            'form':form,
        }
        )

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

def signup(request):
    """signup view"""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = SignupForm()

    return render(
        request=request, 
        template_name='users/signup.html',
        context={
            'form':form
        }
    )

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
