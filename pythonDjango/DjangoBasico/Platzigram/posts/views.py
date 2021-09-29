""" Posts views """

# Django
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.base import RedirectView

# Form
from posts.forms import PostForm

# Models
from posts.models import Likes, Posts
from user.models import Profile

class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all publish posts"""

    template_name = 'posts/feed.html'
    model = Posts
    ordering = ('-created')
    paginate_by = 10
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
        likes_users = Profile.objects.get(user=self.request.user)
        post_final, create = Likes.objects.get_or_create(post=post_id)
        # post_like, create = Likes.objects.get_or_create(likes_users=likes_users)

        if post_final.likes_users.filter(user=self.request.user).exists():
            like_profile = Likes.objects.get(post=post_id)
            like_profile.likes_users.remove(likes_users)
            print("True")
        else:
            like_profile = Likes.objects.get(post=post_id)
            like_profile.likes_users.add(likes_users)
            print("False")

        # post = Posts.objects.get()    

        return super().get_redirect_url()

