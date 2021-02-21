from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.TextField(max_length=100)
    content = models.TextField()
    # lets us update date, and take timezone into consideration
    date_posted = models.DateField(default=timezone.now)
    # get from db and if user deleted delete their posts
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})