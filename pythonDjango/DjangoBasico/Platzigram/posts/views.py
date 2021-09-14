""" Posts views """

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView

# Form
from posts.forms import PostForm

# Models
from posts.models import Posts

class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all publish posts"""

    template_name = 'posts/feed.html'
    model = Posts
    ordering = ('-created')
    paginate_by = 2
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    """DetailView of posts"""

    template_name = 'posts/detail.html'
    queryset = Posts.objects.all()
    context_object_name = 'post'

class CreatePostView(CreateView):
    """CreateView Posts"""

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context

