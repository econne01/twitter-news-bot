"""This is the main function of twitter-news-bot project

It is intended to be run as a cronjob to periodically scan
for news of interest and Tweet about it
"""
import random
from twitter_bot.service.curator import Curator
from twitter_bot.service.news_reader import NewsReader
from twitter_bot.service.twitter import TwitterService


def main():
    news_reader = NewsReader()
    headlines = news_reader.get_headlines()
    print 'All headlines:'
    print headlines

    curator = Curator()
    interesting_headlines = curator.keep_interesting_items(headlines)

    if interesting_headlines:
        twitter_api = TwitterService()
        twitter_api.post_tweet(random.choice(interesting_headlines)[:140])


if __name__ == '__main__':
    main()
