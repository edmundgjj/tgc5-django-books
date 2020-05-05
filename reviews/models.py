from django.db import models
from django.contrib.auth.models import User
import books.models


# Create your models here.
class Review(models.Model):
    book = models.ForeignKey(books.models.Book, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField(blank=False)
    date = models.DateField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " for " + self.book.title
