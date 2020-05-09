ValorantLFM - Hashtag retweeter
========================

This is a simple twitter hashtag retweeter. Any top level tweets that include a hashtag
defined in your config.ini will automatically be retweeted.


This bot powers https://twitter.com/ValorantLFM


Setup
-----

First you must create a twitter developer account and obtain twitters api access/secret keys.

Once you have these keys, rename example.config.ini to config.ini and update it to include the proper
twitter tokens, and your desired hashtags to follow.

Once your config is created, install your requirements and run it like follows.
```
pip install -r requirements.txt
python retweeter/__init__.py
```



How it works
------------


1. This script will use the twitter api to search for the lastest posts containing the defined hashtag.
2. We will then iterate over those tweets, and validate if they're a top level tweet in reverse chronologic order (oldest to newest).
3. We will keep track of what the last tweet we checked in retweeter/last_known_retweet.txt to avoid attempting to retweet the same tweet too often.
4. Once each hashtag has been looped through, we end the script.

Currently in v1, this script is intended to be setup in a cronjob.
