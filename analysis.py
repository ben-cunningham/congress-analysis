import pandas as pd

tweets = {}

def load_tweets(file_name):
    df = pd.read_csv(file_name)
    
    for index, row in df.iterrows():
        if row['to'] not in tweets:
            tweets[row['to']] = []
        
        tweet = {}
        tweet['sender_handle'] = row['name'],
        tweet['sender_uid'] = row['uid'],
        tweet['tweet'] = row['tweet']
        tweets[row['to']].append(tweet)

if __name__ == '__main__':
    load_tweets('data/tweet_dataA.csv')
    load_tweets('data/tweet_dataB.csv')
