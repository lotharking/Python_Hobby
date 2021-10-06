"""Users view"""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_view
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView, RedirectView

# Models
from django.contrib.auth.models import User
from user.models import Followers, Profile
from posts.models import Posts

# Forms
from user.forms import SignupForm

# Utilities
import pandas as pd

class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view"""

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add users posts to context"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Posts.objects.filter(user=user).order_by('-created')
        context['followers'], create = Followers.objects.get_or_create(user=self.request.user)
        user_consult, create = Followers.objects.get_or_create(user=user)

        context['is_following'] = False
        if context['followers'].another_user.filter(username=kwargs['object']).exists():
            context['is_following'] = True
        else:
            context['is_following'] = False

        update_count = Profile.objects.get(user=user)
        update_count.posts_count = context['posts'].count()
        update_count.followers = Followers.objects.filter(another_user=kwargs['object']).count()
        update_count.following = user_consult.another_user.all().count()
        update_count.save()
        return context

class UserFollowView(LoginRequiredMixin, RedirectView):
    """User redirect follow view"""
    pattern_name = 'users:detail'

    def get_redirect_url(self, *args, **kwargs):
        session_user = User.objects.get(username=self.request.user)
        user_follower = User.objects.get(username=kwargs['username'])
        follow_object, create = Followers.objects.get_or_create(user=session_user)
        check_follower = Followers.objects.filter(another_user=user_follower)

        if follow_object.another_user.filter(username=kwargs['username']).exists():
            add_usr = Followers.objects.get(user=session_user)
            add_usr.another_user.remove(user_follower)
        else:
            add_usr = Followers.objects.get(user=session_user)
            add_usr.another_user.add(user_follower)
        return super().get_redirect_url(*args, **kwargs)

class SignupView(FormView):
    """Users sign up view"""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update the posts"""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'phone_number', 'biography', 'picture']

    def get_object(self):
        """Returns user profile"""
        return self.request.user.profile

    def get_success_url(self):
        """Return to user profile"""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})

class LoginView(auth_view.LoginView):
    """LoginView"""
    template_name = 'users/login.html'

class LogoutView(LoginRequiredMixin, auth_view.LogoutView):
    """Logout view"""
    template_name = 'users/logged_out.html'

class DetailUsersView(LoginRequiredMixin, DetailView):
    """Staff detail all users"""

    template_name = 'users/detail_users.html'
    queryset = User.objects.all()
    context_object_name = 'user'
    print(queryset)

