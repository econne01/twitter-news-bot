"""This is the handler for the main function of twitter-news-bot project

It is intended to be run as a cronjob to periodically scan
for news of interest and Tweet about it
"""
from twitter_bot.bot import Bot
from sys import path


def get_interesting_news(event, context):
    print(path)
    # bot = Bot(debug=False)
    # bot.get_interesting_news()

def post_interesting_news():
    bot = Bot(debug=False)
    bot.post_interesting_news()
