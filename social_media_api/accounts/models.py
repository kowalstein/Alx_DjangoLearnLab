from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='follower', blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followings')

    def __str__(self):
        return self.username
