"""This is the main function of twitter-news-bot project

It is intended to be run as a cronjob to periodically scan
for news of interest and Tweet about it
"""
from twitter_bot.service.news_reader import NewsReader

def main():
    news_reader = NewsReader()
    headlines = news_reader.get_headlines()
    print headlines[0]


if __name__ == '__main__':
    main()
