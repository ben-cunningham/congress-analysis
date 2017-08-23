import os
import re

import pandas as pd
import twitter

consumer_key = os.environ['TWTTR_CONSUMER_KEY']
consumer_secret = os.environ['TWTTR_CONSUMER_SECRET']
access_token = os.environ['TWTTR_ACCESS_KEY']
access_secret = os.environ['TWTTR_ACCESS_SECRET']

api = twitter.Api(consumer_key=consumer_key,
                        consumer_secret=consumer_secret,
                        access_token_key=access_token,
                        access_token_secret=access_secret,
                        sleep_on_rate_limit=True)

def process_and_clean(text):
    # get rid of newlines
    text = text.strip().replace("\n", " ").replace("\r", " ")

    # replace twitter @mentions
    mention_finder = re.compile(r"@[a-z0-9_]{1,15}", re.IGNORECASE)
    text = mention_finder.sub("", text)
    
    # remove urls
    url_finder = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', re.IGNORECASE)
    text = url_finder.sub("", text)

    # replace HTML symbols
    text = text.replace("&amp;", "and").replace("&gt;", ">").replace("&lt;", "<")

    # lowercase
    text = text.lower()

    # remove white space
    text = text.strip()

    return text

def get_tweet(row):
    result = None
    try:
        result = api.GetStatus(row['status_id'])
    except:
        print "Could not get results for " +row['name']
        return

    text = process_and_clean(result.text).encode('utf-8')
    tweet_row = [[row['name'], str(row['status_id']), row['to'], text]]
    # print tweet_row
    df = pd.DataFrame(tweet_row, columns=['a','b','c','d'])
    df.to_csv('tweet_data.csv', mode='a', index=False, header=False)

def get_tweets():
    df = pd.read_csv('data.csv')
    df.apply(get_tweet, axis=1)

if __name__ == '__main__':
    get_tweets()
