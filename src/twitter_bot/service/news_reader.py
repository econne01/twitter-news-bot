"""An aggregator service to collect headlines from all news API services"""
from twitter_bot.service.news.new_york_times import NewYorkTimesService

class NewsReader(object):

    def __init__(self):
        self.news_services = [
            NewYorkTimesService()
        ]

    def get_headlines(self):
        headlines = []
        for api_service in self.news_services:
            headlines.extend(api_service.get_latest_headlines())
        return headlines
