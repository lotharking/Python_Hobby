"""Platzigram middleware catalog"""

# Django
from django.shortcuts import redirect
from django.urls import reverse

# Models
from user.models import Profile

class ProfileCompletionMiddleware:
    """Profile completion middleware.

    Ensure every user that is interacting with the platform
    have their profile picture and biography.
    """
    def __init__(self, get_response):
        """Middleware initialization"""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called"""
        if not request.user.is_anonymous:
            # if not request.user.is_staff:
            has_customer = False
            try:
                profile = request.user.profile
            except Profile.DoesNotExist:
                profile = Profile(user=request.user)
                profile.save()
                pass
            # return has_customer and (self.car is not None)
            # if not request.user.profile:
            if not profile.picture or not profile.biography:
                if request.path not in [reverse('users:update'), reverse('users:logout')]:
                    return redirect('users:update')
            # else:
            #     return redirect('users:signup')

        response = self.get_response(request)

        return response