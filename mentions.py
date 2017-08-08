import os

import pandas as pd
import got

def get_tweet_history(handle):
    if handle == None  or len(handle) <= 1:
        return []

    criteria = got.manager.TweetCriteria().setQuerySearch(handle).setSince("2016-05-01")
    results = got.manager.TweetManager.getTweets(criteria)
    
    tweets = []
    for tweet in results:
        tweets.append((tweet.username, tweet.id, handle))
    
    return tweets

def get_tweets(df):
    tweets = []
    for i, row in df.iterrows():
        tweets.extend(get_tweet_history(row.Handle))

    return tweets

def collect_data():
    tweets = []
    reps = pd.read_csv('representatives.csv')
    tweets.extend(get_tweets(reps))

    sens = pd.read_csv('senators.csv')
    tweets.extend(get_tweets(sens))
    
    return pd.DataFrame(tweets, columns=['username', 'tweet_id', 'congressman'])

if __name__ == '__main__':
    data = collect_data()
    data.to_csv('data.csv', index=False)
