from django.db import models
# from ../.users import models as usermodel

from PIL import Image

class Book(models.Model):
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    description = models.TextField()
    book_pic = models.ImageField(upload_to='books', default="book/book_profile.png", blank=True, null=True)
    # readers = models.ManyToManyField(usermodel.User)

    def __str__(self):
        return self.name
