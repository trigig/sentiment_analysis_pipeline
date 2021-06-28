import pymongo
import vaderSentiment
import sqlalchemy 
import logging
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import psycopg2
import time

def extract():
    ''' Extract tweets from mongodb
    how often to extract!
    '''
    extracted_tweets = list(tweets.find()) # add query to check only for new tweets , onlx one we are interested in.
    extracted_tweets = [tweet['text'] for tweet in extracted_tweets] 

    return extracted_tweets

def transform(extracted_tweets):
    '''Perform desired transformation ex. sentiment analysis'''
    transformed_tweet = []
    compound_score = []
    s = SentimentIntensityAnalyzer()
    for tweet in extracted_tweets:
        transformed_tweet.append(tweet)
        score = s.polarity_scores(tweet)
        compound_score.append(score['compound'])
        

    return transformed_tweet, compound_score

def load(transformed_tweet,compound_score):
    ''' loads transformed tweets and analysis into postgres'''
    df = pd.DataFrame({'tweet': transformed_tweet,'score':compound_score}) 
    df.to_sql(name='tweets', con = engine, if_exists='append', index = False)
         
    
if __name__ == '__main__':
      
    ## Create mongodb connection
    
    client = pymongo.MongoClient("mongodb")
    db_mongo = client.tweets
    tweets = db_mongo.tweet_data     
        # create connection to database

    engine = sqlalchemy.create_engine('postgresql://postgres:1234@pgdb:5432/postgres')
    create_query ='CREATE TABLE IF NOT EXISTS tweets(tweet TEXT, score FLOAT);'
    engine.execute(create_query)  

    while True:
        extracted_tweets = extract()
        transformed_tweet, compound_score = transform(extracted_tweets)
        load(transformed_tweet,compound_score)
        logging.critical('Load complete')
        time.sleep(300)


