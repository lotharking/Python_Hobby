""" Posts views """

# Django
from posts.models import Posts
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

# Utilities
from datetime import datetime

# Form
from posts.forms import PostForm

@login_required
def list_posts(request):
    """ List existing post """
    posts = Posts.objects.all().order_by('-created')
    return render(request, 'posts/feed.html', {'posts': posts})

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

