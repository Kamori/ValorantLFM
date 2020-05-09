from valorantlfm import retweet_tags

if __name__ == "__main__":
    retweet_tags()

    # cfg = ConfigParser()
    # cfg.read(f"{os.path.dirname(os.path.realpath(__file__))}/config.ini")

    # consumer_key = cfg["twitter"]["consumer_key"]
    # consumer_secret = cfg["twitter"]["consumer_secret"]
    # access_token = cfg["twitter"]["access_token"]
    # access_token_secret = cfg["twitter"]["access_token_secret"]

    # auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_token_secret)

    # api = tweepy.API(auth)

    # Retweeter(api, exact_tags=["#ValorantLFG", "#ValorantLFM"])
