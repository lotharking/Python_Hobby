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

# class DetailFeedView(LoginRequiredMixin, DetailView):
#     """DetailView of posts"""

#     template_name = 'users/detail.html'
#     slug_field = 'username'
#     slug_url_kwarg = 'slug'
#     queryset = User.objects.all()
#     context_object_name = 'user'

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

