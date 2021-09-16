"""User models"""

# Django
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    """ Profile model
    Proxy model that extends the base data with  other information """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    phone_number=models.CharField(max_length=20,blank=True)
    posts_count = models.PositiveIntegerField(default=0)
    followers = models.PositiveIntegerField(default=0)
    following = models.PositiveIntegerField(default=0)
    picture = models.ImageField(
        upload_to='user/pictures', 
        blank=True, 
        null=True
        )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """return username """
        return self.user.username

class Followers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    another_user = models.ManyToManyField(User, related_name='another_user')

    def __str__(self):
        return self.user.name