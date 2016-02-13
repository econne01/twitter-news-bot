"""This is the main function of twitter-news-bot project

It is intended to be run as a cronjob to periodically scan
for news of interest and Tweet about it
"""
import argparse
import random

from twitter_bot.service.curator import Curator
from twitter_bot.service.news_reader import NewsReader
from twitter_bot.service.twitter import TwitterService


def _get_command_args():
    parser = argparse.ArgumentParser(description='''
        Command for Twitter Bot to scan news sources, find an interesting
        piece of news and tweet about it
    ''')
    parser.add_argument('--debug', action='store_true')
    return parser.parse_args()

def main():
    command_args = _get_command_args()

    news_reader = NewsReader()
    headlines = news_reader.get_headlines()

    curator = Curator()
    interesting_headlines = curator.keep_interesting_items(headlines)

    if interesting_headlines:
        tweet = random.choice(interesting_headlines)
        if command_args.debug:
            print tweet
        else:
            twitter_api = TwitterService()
            twitter_api.post_tweet(tweet)
    else:
        print 'No interesting news found'


if __name__ == '__main__':
    main()
