from django.db import models
from django.urls import reverse
from users.models import User

from PIL import Image

class Book(models.Model):
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    description = models.TextField()
    description2 = models.TextField(blank=True)
    book_pic = models.ImageField(upload_to='books', default="book/book_profile.png", blank=True, null=True)
    readers = models.ManyToManyField(User)

    def __str__(self):
        return self.name
