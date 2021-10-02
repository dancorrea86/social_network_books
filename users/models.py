from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='users/',default='users/default_avatar.png', blank=True, null=True)
    


