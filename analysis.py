import pandas as pd

tweets = {}

def load_tweets(file_name):
    df = pd.read_csv(file_name, nrows=100)
    
    for index, row in df.iterrows():
        if row.isnull().values.any():
            continue
        if row['to'] not in tweets:
            tweets[row['to']] = []
        tweet = {}
        tweet['id'] = row['uid'],
        tweet['from'] = row['name'],
        tweet['text'] = row['tweet']
        tweets[row['to']].append(tweet)

def count_tweets():
    data = []
    for key, value in tweets.iteritems():
        cnt = len(value)
        
        avg_len = 0
        engagers = set()
        for tweet in value:
            avg_len += len(tweet['text'])
            engagers.add(tweet['from'])

        avg_len /= cnt
        data.append((key, cnt, avg_len, len(engagers)))
    
    df = pd.DataFrame(data, columns=['handle', 'total_no_of_tweets', 'avg_len_tweets', 'unique_engagers'])
    df.to_csv('stats.csv', index=False)

if __name__ == '__main__':
    load_tweets('data/tweet_dataA.csv')
    load_tweets('data/tweet_dataB.csv')

    count_tweets()
