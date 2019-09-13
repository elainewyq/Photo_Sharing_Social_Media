# Analysis on the Popularity and Attitude of Three Photo-Sharing Social Media Platforms

## Project Description
Exploratory data analysis on tweets mentioning three photo-sharing social media platforms (Pinterest, Instagram and Snapchat), focusing on the popularity and text sentiment analysis.

## Data
1. number (to update) of tweets filtered by keywords of pinterest, instagram and snapchat, collected from 9/10/2019 10am to (in process) (pacific time)
2. number (to update) of entries with 8 features ('id_str','created_at','text','user_created_at','user_location', 'user_followers_count','user_friends_count', 'longitude','latitude')

## Objectives
1. Explore the popularity of the three photo-sharing platforms 
2. Use sentiment analysis to understand users' feelings towards the platforms

## Pipeline and EDA
1. Collect tweets by a filter of "english only" and keywords (pinterest, instagram and snapchat). For example, a tweet posted between the timeframe stated above with any feature mentioning 'pinterest' will be downloaded and stored to the subgroup PinterestData.txt.
2. Clean up the text with function 'deEmojify' and 'clean_tweet', which delete all emojies and unusual signs in tweets
3. Read in the data as Pandas DataFrame
4. Take a overview of the dataset, handle missing values and set each feature in an appropriate format/type
5. Perform EDA and visulize the result
6. Perform sentiment analysis on text, excluding retweets. (Tool: NLTK; Source: Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.)
7. Perform more EDA based on sentiment analysis result


## Hypothesis Testing
1. Difference in the count of users' followers and friends for tweets related to different platforms (Non-parametrics: Mann-Whitney signed rank test)
2. Difference in the sentiment of tweets related to different platforms (Non-parametrics: Mann-Whitney signed rank test)
3. to add more...

