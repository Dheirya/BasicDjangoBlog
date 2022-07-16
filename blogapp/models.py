from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256, default='Dheirya Tyagi')
    content = models.TextField()
    posted_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
