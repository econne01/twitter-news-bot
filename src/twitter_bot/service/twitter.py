"""Twitter API service for reading or writing to Twitter for Bot's account"""
import oauth2
from twitter_bot.config.api_keys import TWITTER_API_KEYS


class TwitterService(object):

    def __init__(self):
        self.twitter_client = self._get_twitter_client()

    def post_tweet(self, tweet):
        """Post a tweet to Twitter

        @param {String} tweet
        """
        print tweet

    def _get_twitter_client(self):
        consumer = oauth2.Consumer(key=TWITTER_API_KEYS['API_KEY'],
                                   secret=TWITTER_API_KEYS['API_SECRET'])
        token = oauth2.Token(key=TWITTER_API_KEYS['ACCESS_TOKEN'],
                             secret=TWITTER_API_KEYS['ACCESS_SECRET'])
        return oauth2.Client(consumer, token)

