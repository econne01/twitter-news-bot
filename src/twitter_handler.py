"""This is the handler for the main function of twitter-news-bot project

It is intended to be run as a cronjob to periodically scan
for news of interest and Tweet about it
"""
from twitter_bot.bot import Bot


def get_interesting_news(event, context):
    bot = Bot(debug=False)
    headline = bot.get_interesting_news()
    print(headline)
    return headline

def post_interesting_news():
    bot = Bot(debug=False)
    bot.post_interesting_news()

if __name__ == '__main__':
    get_interesting_news('', '')
