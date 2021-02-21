from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from .tweepy_CODE import Tweet
from . import config



class Post(models.Model):
    title = models.TextField(max_length=100)
    summary = models.TextField(max_length=240, default="A post about fair trade")
    content = models.TextField()
    # lets us update date, and take timezone into consideration
    date_posted = models.DateField(default=timezone.now)
    # get from db and if user deleted delete their posts
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs) 
        api = initKeys(Tweet)
        api.send_tweet(content)

    def initKeys(script):
        consumer_key = config.Twitter['Consumer_Key']
        consumer_secret = config.Twitter['Consumer_Secret']
        access_token = config.Twitter['Access_Token']
        access_token_secret = config.Twitter['Access_Secret']
        return script(consumer_key,consumer_secret,access_token,access_token_secret)
        