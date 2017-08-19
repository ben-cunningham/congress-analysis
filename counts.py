consumer_key = os.environ['TWTTR_CONSUMER_KEY']
consumer_secret = os.environ['TWTTR_CONSUMER_SECRET']
access_token = os.environ['TWTTR_ACCESS_KEY']
access_secret = os.environ['TWTTR_ACCESS_SECRET']

def get_tweets():
    api = twitter.Api(consumer_key=consumer_key,
                        consumer_secret=consumer_secret,
                        access_token_key=access_token,
                        access_token_secret=access_secret)

    results = api.GetSearch(term='@SenKamalaHarris')
    print(results)

if __name__ == '__main__':
    get_tweets()
