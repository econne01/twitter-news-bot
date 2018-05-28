"""Twitter API service for reading or writing to Twitter for Bot's account"""
import json
import urllib
import oauth2
from twitter_bot.config.api_keys import TWITTER_API_KEYS
from twitter_bot.constants import TWEET_CHAR_LIMIT, TWITTER_USERNAME
from twitter_bot.service.url_shortener import get_long_url


class TwitterService(object):

    def __init__(self):
        self.twitter_client = self._get_twitter_client()

    def get_recently_tweeted_headlines(self, tweet_count=20):
        """Return a list of headlines that have been tweeted in the past given number of tweets

        @param {integer} tweet_count
        """
        headlines = []
        tweets = self._get_recent_tweets(tweet_count)
        for tweet in tweets:
            for tweeted_url in tweet['entities']['urls']:
                url = tweeted_url['expanded_url']
                if 'goo.gl' in url:
                    headlines.append(get_long_url(url))
                else:
                    headlines.append(url)
        return list(set(headlines))

    def post_tweet(self, tweet):
        """Post a tweet to Twitter

        @param {String} tweet
        """
        POST_URL = 'https://api.twitter.com/1.1/statuses/update.json'
        post_data = {
            'status': tweet[:TWEET_CHAR_LIMIT]
        }
        response, content = self.twitter_client.request(POST_URL, method='POST',
                                                        body=urllib.parse.urlencode(post_data))
        return response

    def _get_recent_tweets(self, tweet_count=20):
        """Return a list of JSON objects representing the latest given number of tweets

        @param {integer} tweet_count
        """
        TIMELINE_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'
        get_params = {
            'screen_name': TWITTER_USERNAME,
            'count': tweet_count
        }
        GET_URL = TIMELINE_URL + '?{params}'.format(params=urllib.parse.urlencode(get_params))
        resp, content = self.twitter_client.request(GET_URL, method='GET')
        return json.loads(content)

    def _get_twitter_client(self):
        consumer = oauth2.Consumer(key=TWITTER_API_KEYS['API_KEY'],
                                   secret=TWITTER_API_KEYS['API_SECRET'])
        token = oauth2.Token(key=TWITTER_API_KEYS['ACCESS_TOKEN'],
                             secret=TWITTER_API_KEYS['ACCESS_SECRET'])
        return oauth2.Client(consumer, token)
