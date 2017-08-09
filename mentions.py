import os

import pandas as pd
import got

politician_count = 0
tweet_count = 0

def get_tweet_history(handle):
    if handle == None  or len(handle) <= 1:
        return []

    criteria = got.manager.TweetCriteria().setQuerySearch(handle).setSince("2016-05-01")
    count = 5
    results = []
    while count > 0:
        try:
            results = got.manager.TweetManager.getTweets(criteria)
            break
        except:
            count -= 1
    
    if len(results) == 0:
        return []
    
    tweets = []
    for tweet in results:
        tweets.append((tweet.username, tweet.id, handle))
    
    return tweets

def get_tweets(df):
    tweets = []
    for i, row in df.iterrows():
        hist = get_tweet_history(row.Handle)
        tweets.extend(hist)

        global politician_count
        politician_count += 1
        global tweet_count
        tweet_count += len(hist)

        print("Politician Count: " +str(politician_count))
        print("Tweet Count: " +str(tweet_count))

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
