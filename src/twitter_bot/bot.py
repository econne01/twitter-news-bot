"""
Twitter Bot to embody Curbo bot's thoughts and actions
and to coordinate the various services and components of code
"""
from twitter_bot.service.curator import Curator
from twitter_bot.service.news_reader import NewsReader
from twitter_bot.service.twitter import TwitterService


class Bot(object):

    def __init__(self, debug=False):
        self.curator = Curator()
        self.reader = NewsReader()
        self.debug_mode = debug

    def post_interesting_news(self):
        """Scan news for interesting items and post (ie, Tweet) about one"""
        headlines = self.reader.get_headlines()

        interesting_headlines = self.curator.keep_interesting_items(headlines)

        if interesting_headlines:
            tweet = random.choice(interesting_headlines)
            if self.debug_mode:
                print tweet
            else:
                twitter_api = TwitterService()
                twitter_api.post_tweet(tweet)
        else:
            print 'No interesting news found'


