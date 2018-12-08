import tweepy
from textblob import TextBlob

consumer_key = 'CONSUMER-KEY-HERE'
consumer_secret = 'CONSUMER-SECRET-HERE'

access_token = 'ACCESS-TOKEN-HERE'
access_token_secret = 'ACCESS-TOKEN-SECRET-HERE'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('India')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)