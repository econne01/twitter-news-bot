"""Twitter API service for reading or writing to Twitter for Bot's account"""
import oauth2
import urllib
from twitter_bot.config.api_keys import TWITTER_API_KEYS
from twitter_bot.constants import TWEET_CHAR_LIMIT


class TwitterService(object):

    def __init__(self):
        self.twitter_client = self._get_twitter_client()

    def post_tweet(self, tweet):
        """Post a tweet to Twitter

        @param {String} tweet
        """
        POST_URL = 'https://api.twitter.com/1.1/statuses/update.json'
        post_data = {
            'status': tweet[:TWEET_CHAR_LIMIT]
        }
        response, content = self.twitter_client.request(POST_URL, method='POST',
                                                        body=urllib.urlencode(post_data))
        return response

    def _get_twitter_client(self):
        consumer = oauth2.Consumer(key=TWITTER_API_KEYS['API_KEY'],
                                   secret=TWITTER_API_KEYS['API_SECRET'])
        token = oauth2.Token(key=TWITTER_API_KEYS['ACCESS_TOKEN'],
                             secret=TWITTER_API_KEYS['ACCESS_SECRET'])
        return oauth2.Client(consumer, token)

