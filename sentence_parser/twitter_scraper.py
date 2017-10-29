import twitter
import pprint

class Twitter:

    def __init__(self):
        self.api = twitter.Api(consumer_key=('QkIapOR0x3RmbUAF2gCOvhsZB'),
                               consumer_secret=('MIsXmNhK88wNvJ201RMBt0nAS3quJxxeKw2yzJZTuaEKtZU9nW'),
                               access_token_key=('924530444544217088-zWEM1N867VW6bRFPPlok09rrMqOCGUs'),
                               access_token_secret=('zzbzgi27xb5bFoYqbick8CkKNA70w81GUFqdqptaVjLDb'))
        return

    def get_search(self, query, count, tweet_id=''):
        return self.api.GetSearch(raw_query='q={}%20&count={}&id={}'.format(query, count, tweet_id))

    def get_text(self, query, count):
        item_list = list()
        tweet_id = ''
        tweet_id_local = ''
        for i in range(0, count, 100):
            for item in self.get_search(query, count, tweet_id):
                text, tweet_id_local = item.text, item.id
                item_list.append(text)
            tweet_id = tweet_id_local
        return item_list

# twit = Twitter()
# counter = 0
# tweets = twit.get_text('Trump', 10000)
# for tweet in tweets:
#     counter = counter + 1
#     print(tweet.split('\'')[0])
# print(counter)
