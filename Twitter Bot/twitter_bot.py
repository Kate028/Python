# This Python Bot will retweet and like specific hashtag and mention
# install tweepy using pip install tweepy
# import the required modules
import tweepy
import time

# Import Twitter application keys, tokens, and secrets from keys.py.
from keys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# test authentication
api.verify_credentials() 
print("Authentication Successful") 

# hashtag and mention that you want to retweet
search = "kate028" and "kate028_"
nfTweets = 100

for tweet in tweepy.Cursor(api.search_tweets, search).items(nfTweets):
    try:
        tweet.favorite()
        print('Liked')
        tweet.retweet()
        print('Retweeted')
        tweet.sleep(10) # 10(in sec) is the time you want to have in-between retweets.
    except StopIteration:
        break

    # Some basic error handling. Will print out why retweet failed, into your terminal.
    # except tweepy.errors.TweepyException as error:
    #     print('\nError. Retweet not successful. Reason: ')
    #     print(error.reason)
