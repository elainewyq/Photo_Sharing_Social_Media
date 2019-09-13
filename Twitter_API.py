'''
Purpose:
Below is the API used to stream the real-time tweets

Sources:
Twitter API: https://developer.twitter.com/en/docs/api-reference-index
Tweepy document: http://docs.tweepy.org/en/latest/streaming_how_to.html

Note:
Here I use the streamer for Instagram as an example. In order to filter 
another two platforms (pinterest and snapchat) and save them separately, I open
another two streamers and run them at the same time to collect data for the two platforms

'''

import pandas as pd
import tweepy
from textblob import TextBlob
import re
import credentials
import OpenSSL
import time
import TweetsFunction as TF 



f = open("InstagramData.txt", "a")

count = 0

class MyStreamListener(tweepy.StreamListener):

    # Extract info from tweets
    def on_status(self, status):
        if status.retweeted:
            # Avoid retweeted info, and only original tweets will 
            # be received
            return True
        # Extract attributes from each tweet
        id_str = status.id_str
        created_at = status.created_at
        text = TF.deEmojify(status.text)    # Pre-processing the text  
        text = TF.clean_tweet(text)


        user_created_at = status.user.created_at
        user_location = status.user.location
        user_followers_count =status.user.followers_count
        user_friends_count =status.user.friends_count

        longitude = None
        latitude = None
        if status.coordinates:
            longitude = status.coordinates['coordinates'][0]
            latitude = status.coordinates['coordinates'][1]

        retweet_count = status.retweet_count
        favorite_count = status.favorite_count

        # Quick check contents in tweets
        delimiter = '\t'
        text = text.replace(delimiter, ' ').replace('\n', ' ')
        fields = [id_str, created_at, text, user_created_at, user_location, user_followers_count,
                                                                user_friends_count, longitude, latitude, retweet_count, favorite_count]
        
        f.write(delimiter.join(map(str, fields)) + '\n')
        f.flush()
        global count
        if count % 50 == 0:
            print('processed %s messages' % count)
        count += 1

        
    def on_error(self, status_code):
        '''
        Since Twitter API has rate limits, 
        stop srcraping data as it exceed to the thresold.
        '''
        if status_code == 420:
            # return False to disconnect the stream
            return False


# Import api/access_token keys from credentials.py

auth  = tweepy.OAuthHandler(credentials.API_KEY,
                            credentials.API_SECRET_KEY)
auth.set_access_token(credentials.ACCESS_TOKEN,
                      credentials.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


# the stream listener won't stop automatically. 
# Press STOP button to finish the process.
while True:
    try:
        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth = api.auth, listener = myStreamListener)
        TRACK_WORDS = ['instagram']
        myStream.filter(languages=["en"], track = TRACK_WORDS)
    except Exception as e:
        print(e)
        time.sleep(30)