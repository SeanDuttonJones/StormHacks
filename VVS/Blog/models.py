from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # lets us update date, and take timezone into consideration
    date_posted = models.DateField(default=timezone.now())
    # get from db and if user deleted delete their posts
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = 'Nate the Great'
