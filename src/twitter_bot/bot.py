"""
Twitter Bot to embody Curbo bot's thoughts and actions
and to coordinate the various services and components of code
"""
import random

from twitter_bot.constants import REPEAT_HEADLINE_MIN_TWEET_LIMIT
from twitter_bot.service.curator import Curator
from twitter_bot.service.news_reader import NewsReader
from twitter_bot.service.twitter import TwitterService
from twitter_bot.service.url_shortener import get_short_url


class Bot(object):

    def __init__(self, debug=False):
        self.curator = Curator()
        self.reader = NewsReader()
        self.twitter_api = TwitterService()
        self.debug_mode = debug

    def post_interesting_news(self):
        """Scan news for interesting items and post (ie, Tweet) about one"""
        news_bites = self.reader.get_news()

        interesting_news = self.curator.keep_interesting_items(news_bites)
        if interesting_news:
            interesting_news = self._filter_out_old_news(interesting_news)
            news_bite = random.choice(interesting_news)
            tweet = self._generate_tweet(news_bite)

            if self.debug_mode:
                print tweet
            else:
                self.twitter_api.post_tweet(tweet)
        else:
            print 'No interesting news found'

    def _filter_out_old_news(self, news_bites):
        """Filter out any news bites that have already been tweeted in the past 100 tweets"""
        old_news_headlines = self.twitter_api.get_recently_tweeted_headlines(
            REPEAT_HEADLINE_MIN_TWEET_LIMIT)
        return [news_bite for news_bite in news_bites if news_bite.url not in old_news_headlines]

    def _generate_tweet(self, news_bite):
        """Generate Tweet text from a NewsBite instance"""
        short_url = get_short_url(news_bite.url)
        if news_bite.headline:
            max_chars = max(0, 140-1-len(short_url))
            tweet = news_bite.headline[:max_chars] + ' ' + short_url
        else:
            tweet = 'Wow! ' + short_url
        return tweet

