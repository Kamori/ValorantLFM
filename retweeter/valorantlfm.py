# This script will query Twitter for the latest tweets using a given hashtag
# Based on each run it will commit the last analyzed tweet to disk, so we
# can look for all newer tweets after that.


# GOTCHAS: If 150 new tweets come in since the last analyzed tweet, we may
# have a gap in tweets we can review. This problem doesn't exist until we make
# our hashtags popular though.


import logging
import os
from configparser import ConfigParser
from pprint import pprint

import tweepy

from brain import Brain

cfg = ConfigParser()
cfg.read(f"{os.path.dirname(os.path.realpath(__file__))}/config.ini")

consumer_key = cfg["twitter"]["consumer_key"]
consumer_secret = cfg["twitter"]["consumer_secret"]
access_token = cfg["twitter"]["access_token"]
access_token_secret = cfg["twitter"]["access_token_secret"]
TAGS = [htag.strip() for htag in cfg["twitter"]["hashtags"].split(",")]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

API = tweepy.API(auth)
LAST_TWEET_FILE = (
    f"{os.path.dirname(os.path.realpath(__file__))}/last_known_retweet.txt"
)
BRAIN = Brain(LAST_TWEET_FILE)

FORMAT = "%(asctime)-15s:%(levelname)s:%(pathname)s:%(funcName)s:%(lineno)d: %(message)s"
logging.basicConfig(format=FORMAT, datefmt="%Y-%m-%d:%H:%M:%S")
logger = logging.getLogger(__name__)


def _is_tweet_toplevel(tweet):
    """is_tweet_toplevel detects if a tweet is a top level tweet.
    Top level tweets are identified by not being a response to another tweet, 
    or being a retweet of another tweet.

    Args:
        tweet ([Status]): A tweepy Status object
    
    Returns:
        bool
    """

    reply_to = tweet.in_reply_to_status_id
    retweet_of = getattr(tweet, "retweeted_status", None)

    # If the tweet is a reply to another tweet, or a retweet of a different
    # tweet, it is not top level
    if reply_to or retweet_of:
        return False

    return True


def _retweet(tweet):
    tweet.retweet()
    return None


def _get_sinceid_for_tag(tag):
    return BRAIN[tag].get("id_str", None)


def _set_tag_to_tweet(tag, tweet):
    BRAIN[tag] = tweet


def _save_brain():
    BRAIN.save_file()


def retweet_tags():

    for tag in TAGS:
        print(f"Now searching for tag: {tag}")
        last_tweet_id = _get_sinceid_for_tag(tag)
        public_tweets = API.search(q=tag, count=500, since_id=last_tweet_id)

        for tweet in reversed(public_tweets):
            print("======")
            print(f"{tweet.author.name}: ")
            print(f"{len(tweet.text)}")
            print(_is_tweet_toplevel(tweet))
            if _is_tweet_toplevel(tweet):
                try:
                    _retweet(tweet)
                    print("I retweeted that")

                except Exception as e:
                    print(f"I got {e}")
                    pass
            print("------")

            # Done looking at tweet, now update our brain
            print(f"Updating brainfile to tweet id: {tweet.id}")
            _set_tag_to_tweet(tag, tweet._json)

        _save_brain()
        print("Brain saved, moving on")

    print("Loop done, good-bye!")


#################


# class Retweeter:
#     def __init__(self, tweepyapi, exact_tags=None, like_tags=None, brain=None):
#         self.api = tweepyapi
#         self.exact_tags = exact_tags
#         self.like_tags = like_tags

#         if self.like_tags:
#             logger.warning("Retweeting like tags is currently not supported")

#     def search_for_string(self, string, since_id=None):
#         result = self.api.search(q=string, count=500, since_id=since_id)
#         return reversed([Tweet(tweet) for tweet in result])

# class Tweet(tweepy.Tweet):

#     def __init__(self, tweet):
#         self.tweet = tweet


# def functional_section():
#     myrt = Retweeter(api, exact_tags=['1', '2'])
#     mybrain = Brain(LAST_TWEET_FILE)
#     for tag in ["#ValorantLFG", "#ValorantLFM"]:
#         myrt.search_for_string(tag, since_id=mybrain[tag].get("id_str", None)

# ###
# #  myretweeter = retweeter('#ValorantLFG', '#ValorantLFM')
# #  retweet_tags(*tags)
