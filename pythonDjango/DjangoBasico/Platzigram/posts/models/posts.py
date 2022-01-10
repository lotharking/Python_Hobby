"""Posts models"""

# Django
from user.models import Profile
from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    """Post model"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    likes_users = models.ManyToManyField(User, related_name='likes_users')

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photo')

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Post'

    def __str__(self):
        """Return title and username"""
        return '{} by @{}'.format(self.title, self.user.username)

# class Likes(models.Model):
#     post = models.OneToOneField(Posts, on_delete=models.CASCADE)

#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.post.title