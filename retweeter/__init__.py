from configparser import ConfigParser

import tweepy

cfg = ConfigParser()
cfg.read("./retweeter/config.ini")

consumer_key = cfg["twitter"]["consumer_key"]
consumer_secret = cfg["twitter"]["consumer_secret"]
access_token = cfg["twitter"]["access_token"]
access_token_secret = cfg["twitter"]["access_token_secret"]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
