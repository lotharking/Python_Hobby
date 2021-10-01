""" Posts views """

# Django
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import RedirectView
from django.db.models import Q 

# Form
from posts.forms import PostForm

# Models
from django.contrib.auth.models import User
from posts.models import Posts
from user.models import Profile

class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all publish posts"""

    template_name = 'posts/feed.html'
    model = Posts
    ordering = ('-created')
    paginate_by = 10
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        """Update the post context"""
        context = super().get_context_data(**kwargs)
        context['value'] = False
        return context

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

    def form_valid(self, form):
        """Form validate"""
        form.save()
        update_count = Profile.objects.get(user=self.request.user)
        update_count.posts_count = Posts.objects.filter(user=self.request.user).count()
        update_count.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """Update the post context"""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context

class LikePostView(LoginRequiredMixin, RedirectView):
    """Likes to post"""

    pattern_name = 'posts:feed'

    def get_redirect_url(self, *args, **kwargs):
        """add like before url"""
        post_id = Posts.objects.get(pk=kwargs['pk'])
        likes_users = User.objects.get(username=self.request.user)
        # print(post_id.likes_users.get)

        if post_id.likes_users.filter(username=self.request.user).exists():
            post_id.likes_users.remove(likes_users)
        else:
            post_id.likes_users.add(likes_users)

        return super().get_redirect_url()

