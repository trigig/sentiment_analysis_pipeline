import config
import tweepy
from tweepy import OAuthHandler, Cursor, API
from tweepy.streaming import StreamListener
import logging
import pymongo
import time

def authenticate():
    """Function for handling Twitter Authentication. Please note
       that this script assumes you have a file called config.py
       which stores the 2 required authentication tokens:

       1. API_KEY
       2. API_SECRET
       See course material for instructions on getting your own Twitter credentials.
    """
    auth = OAuthHandler(config.API_KEY, config.API_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
    return auth

if __name__ == '__main__':
    auth = authenticate()
    api = API(auth)
    client = pymongo.MongoClient("mongodb")
    db = client.tweets
    collection = db.tweet_data  

    while True:
        cursor = Cursor(
            api.user_timeline,
            id = 'nytimes',
            tweet_mode = 'extended'
        )

        for status in cursor.items(20):
            text = status.full_text

            # take extended tweets into account
            # TODO: CHECK
            if 'extended_tweet' in dir(status):
                text =  status.extended_tweet.full_text
            if 'retweeted_status' in dir(status):
                r = status.retweeted_status
                if 'extended_tweet' in dir(r):
                    text =  r.extended_tweet.full_text

            tweet = {
                'text': text,
                'username': status.user.screen_name,
                'followers_count': status.user.followers_count
            }
            logging.critical(tweet)
            collection.insert_one(tweet)
        time.sleep(300)    
      

    