#Functions used to preprocessing tweets

import pandas as pd
import tweepy
from textblob import TextBlob
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def deEmojify(text):
    '''
    The function consumes text and delete emoji in the input.
    '''
    if text:
        return text.encode('ascii', 'ignore').decode('ascii')
    else:
        return None
    
def clean_tweet(tweet): 
    ''' 
    Use sumple regex statemnents to clean tweet text by removing links and special characters
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) \
                                |(\w+:\/\/\S+)", " ", tweet).split())

def sentiment(sentence): 
    '''
    use this function to get sentiment score for the input sentence, the score is assigned by the NLTK model
    '''   
    sentiment = SentimentIntensityAnalyzer()
    score = sentiment.polarity_scores(sentence)
    return score                       

def bootstrap(sample_df):
  '''
  This function is used to generate sample from the input sample dataframe.
  The return is a list of lists (each element list is an entry randomly selected from the input dataframe)
  '''
    sample_list = sample_df.values.tolist()
    sample_size = len(sample_df)
    get_sample = []
    
    random_select = np.random.randint(0, (sample_size -1), sample_size)
    for j in random_select:
        get_sample.append(sample_list[j])
    
    return get_sample

def relatively_positive_ratio(sample_list):
  '''
  This function is used to calculate the relatively positive ratio for each sample
  The input is the NLTK sentiment analysis result
  The output is the ratio of positive tweets amount divided by the sum of positive twees count and negative tweets count
  Please refer to presentation slides for definition
  '''
    positive_count = 0
    negative_count = 0
    for i in sample_list:
        if i[2] > 0.5:
            negative_count += 1
        elif i[4] > 0.5:
            positive_count += 1
    if positive_count + negative_count == 0:
        return 0
    else:
        return positive_count/(positive_count + negative_count)