import tweepy
import re
import csv
import os
from datetime import date
import json

from urllib.parse import urlparse
    
class Tweet():
    
    def __init__(self,consumer_key,consumer_secret,access_token,access_token_secret):
        """
        Get the keys
        """
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret


    def Auth(self):
        """
        Make sure the keys work
        """
        try:
            self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
            self.auth.set_access_token(self.access_token, self.access_token_secret)
            self.api = tweepy.API(self.auth,wait_on_rate_limit=True)
        except tweepy.error.TweepError:
            print("Something is wrong with one of your keys from Twitter")   

    def send_tweet(self,message):
        self.Auth()
        self.api.update_status(message) 

    
        