# Data Pipeline for Sentiment Analysis on tweets--> posting result as chatbot in Slack  
###About:
This script get tweets from twitter's API for sentiment analysis by using vaderSentiment and post as chatbot in slack.
credits: https://github.com/cjhutto/vaderSentiment

###Main goals:
1. Doing the sentiment analysis with vaderSentiment which is the designed for social media messages.
2. Applying docker contrainer for each step and build docker compose for the whole pipeline.
3. Learn to use mongodb and postgreSQL.

###Process: 
[img](pipeline.jpg)

### The docker-compose contains this following containers:
1) tweet_collector
2) mongodb
3) etl
4) PostgreSQL
5) Slack chatbot

### How to use:
1) tweet_collector need twitter developer credential as config.py
2) webhook_url need to be inserted in chatbot.py
3) Run docker-compose.yml from the project directory --> docker-compose up




