from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(blank=False, max_length=255)
    ISBN = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)

    def __str__(self):
        return self.title
