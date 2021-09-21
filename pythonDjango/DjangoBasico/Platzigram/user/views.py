"""Users view"""

# Django
from django.conf.urls import url
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_view
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views.generic import DetailView, FormView, UpdateView, RedirectView

# Models
from django.contrib.auth.models import User
from user.models import Followers, Profile
from posts.models import Posts

# Forms
from user.forms import SignupForm

class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view"""

    template_name = 'users/detail.html'
    queryset = User.objects.all()
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        """Add users posts to context"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Posts.objects.filter(user=user).order_by('-created')
        context['followers'] = Followers.objects.filter(user=user)
        update_count = Profile.objects.get(user=user)
        update_count.posts_count = context['posts'].count()
        update_count.followers = Followers.objects.filter(another_user=user).count()
        print(Followers.objects.filter(another_user=user).count())
        update_count.save()
        return context

class UserFollowView(LoginRequiredMixin, RedirectView):
    """User follow view"""

    permanent = False
    pattern_name = 'users:detail'

    def get_redirect_url(self, *args, **kwargs):
        # article = get_object_or_404(Article, pk=kwargs['pk'])
        # article.update_counter()
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
        return reverse('users:detail', kwargs={'slug': username})

class LoginView(auth_view.LoginView):
    """LoginView"""
    template_name = 'users/login.html'

class LogoutView(LoginRequiredMixin, auth_view.LogoutView):
    """Logout view"""
    template_name = 'users/logged_out.html'
