# Analysis on the Popularity and Attitude of Three Photo-Sharing Social Media Platforms

## Project Description
Exploratory data analysis on tweets mentioning three photo-sharing social media platforms (Pinterest, Instagram and Snapchat), focusing on the popularity and text sentiment analysis.

## Data
310,419 of tweets filtered by keywords of pinterest, instagram and snapchat, collected from 9/11/2019 5pm to 9/12/2019 01am with 11 features ('id_str','created_at','text','user_created_at','user_location', 'user_followers_count','user_friends_count', 'longitude','latitude', 'retweet_count', 'favorite_count'). Since the tweets are collected real time, the retweet count and favorite count are zero.

## Objectives
1. Explore the popularity of the three photo-sharing platforms 
2. Use sentiment analysis to understand users' feelings towards the platforms

## Pipeline and EDA
1. Collect tweets by a filter of "english only" and keywords (pinterest, instagram and snapchat). For example, a tweet posted between the timeframe stated above with any feature mentioning 'pinterest' will be downloaded and stored to the subgroup PinterestData.txt.
2. Clean up the text with function 'deEmojify' and 'clean_tweet', which delete all emojies and unusual signs in tweets
3. Load the data to Pandas DataFrame
4. Take a overview of the dataset, handle missing values and set each feature in an appropriate format/type
  a. The data consists of - 1.6% of tweets related to Pinterest; 90.5% of tweets related to Instagram; 7.9% of tweets related to Snapchat.
  b. As for the distribution of the tweets, there is not obvious difference between the three platforms 
5. Perform EDA and visulize the result
  a. User_location, longitude, latitude: Only 8% of the users shared the location.
  b. User_followers_count,  User_friends_count: The distribution of the user followers count have long tail. 

6. Perform sentiment analysis on text, excluding retweets. (Tool: NLTK; Source: Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.)
7. Perform more EDA based on sentiment analysis result


## Hypothesis Testing
1. Hypothesis test on popularity
  a. Measurements: Difference in the count of users' followers and friends for tweets related to different platforms 
  b. Mann-Whitney Signed Rank Test: The distribution are highly skewed to the right. It doesn't appear to be normal and the data is imbalanced 
2. Hypothesis test on positivity
  a. Based on the sentiment analysis result from NLTK model, I defined the metric: Relative Positive Ratio = # of positive tweets / (# of positive tweets + # of negative tweets)
  b. Generate more samples by using Bootstrap
  c. Welch's T-test
    i. Why Welch's T-test?
        From the plot of the RPR distribution, I assume the RPR for each platform are normal distributed.
        I performed Welch's t-test rather than student t-test for the following two reasons:
        1) we have no reason to assume the three variances are dependent on the mean of the RPR, which introduces extra uncertainty to the model
        2) we have no reason to assume the three variances are some
    ii. Hypothesis
        (Pints_RPR: The mean of tweets RPR for pinterest 
        Insta_RPR: The mean of tweets RPR for instagram
        Snap_RPR: The mean of tweets RPR for snapchat)

        Null_1 Hypothesis: Pints_RPR = Insta_RPR
        Alternate_1 Hypothesis: Insta_RPR > Pints_RPR 

        Null_2 Hypothesis: Pints_RPR = Snap_RPR
        Alternate_2 Hypothesis: Pints_RPR > Snap_RPR

        Null_3 Hypothesis: Insta_RPR = Snap_RPR
        Alternate_3 Hypothesis: Insta_RPR > Snap_RPR

    iii. Confidence Level
        Confidence Level (Alpha) for the combined test is 0.05. (i.e. the alpha for each test is 0.05/3)
  d. Mann-Whitney Signed Rank Test
     i. After Welch's t-test, I used a non-parametrics test to confirm our conclusion. The Mann-Whitney U-test is a modern alternative to the classical Student's and Welch's t-test that makes good use of modern computing power. It makes no distributional assumptions (unlike the t-test, which assumes the populations are normal), and can always be used instead.  

## Conclusion
1. Popularity
  We used user’s followers count and friends count as measurements of the platform’s popularity, dropped the largest 10% outliers and performed u-test on the measurements. Pinterest > Snapchat != Instagram
  
2. Positivity
  We defined a metric (RPR) to measure the user’s attitude towards each platform and performed t-test and u-test on the difference between each pair of the three platform’s RPR. Pinterest > Instagram > Snapchat
