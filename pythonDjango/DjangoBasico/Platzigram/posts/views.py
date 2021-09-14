""" Posts views """

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

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

    def get_context_data(self, **kwargs):
        """Add users posts to context"""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Posts.objects.filter(user=user).order_by('-created')
        return context

@login_required
def create(request):
    """Create new post view"""

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = PostForm()

    return render(
        request,
        'posts/new.html',
        context={
            'form':form,
            'user':request.user,
            'profile':request.user.profile,
        }
        )

