import requests
import sqlalchemy
import pandas as pd
import psycopg2
import time
import logging
import json



while True:
    engine = sqlalchemy.create_engine('postgresql://postgres:1234@pgdb:5432/postgres')
    df = pd.read_sql_table('tweets', engine)
    df['score'] = df['score'].astype(str)
    data_json = df.to_json(orient= 'records')
    data_json = json.loads(data_json)
    webhook_url = ""
    
    index = 0
    while index <= 500:
        tweet = data_json[index]['tweet']
        score = data_json[index]['score']
        response =requests.post(webhook_url, json = {'text':f"Tweet:\n {tweet}.\n\n Sentiment Score:\n{score}"})
        index +=1
        time.sleep(300)
