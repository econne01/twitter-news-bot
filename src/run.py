"""This is the main function of twitter-news-bot project

It is intended to be run as a cronjob to periodically scan
for news of interest and Tweet about it
"""
from twitter_bot.service.news_reader import NewsReader
from twitter_bot.service.twitter import TwitterService


def main():
    news_reader = NewsReader()
    headlines = news_reader.get_headlines()
    twitter_api = TwitterService()
    twitter_api.post_tweet(headlines[0][:140])


if __name__ == '__main__':
    main()
