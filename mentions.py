import os

import pandas as pd
import got

politician_count = 0
tweet_count = 0

def get_tweet_history(handle):
    if handle == None  or len(str(handle)) <= 1:
        return []

    criteria = got.manager.TweetCriteria().setQuerySearch(handle).setSince("2016-07-01")
    count = 5
    results = []
    while count > 0:
        try:
            print("Getting results for " +handle +"...")
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
    for i, row in df.iterrows():
        hist = get_tweet_history(row.Handle)

        global politician_count
        politician_count += 1
        global tweet_count
        tweet_count += len(hist)

        print("Politician Count: " +str(politician_count))
        print("Tweet Count: " +str(tweet_count))

        df = pd.DataFrame(hist, columns=['username', 'tweet_id', 'congressman'])
        df.to_csv('data.csv', mode='a', index=False, header=False) 

def collect_data():
    tweets = []
    reps = pd.read_csv('representatives.csv')
    # tweets.extend(get_tweets(reps))

    sens = pd.read_csv('senators.csv')
    tweets.extend(get_tweets(sens))
    
if __name__ == '__main__':
    collect_data()
