"""An aggregator service to collect headlines from all news API services"""
from twitter_bot.service.news.new_york_times import NewYorkTimesService

class NewsReader(object):

    def __init__(self):
        self.news_services = [
            NewYorkTimesService()
        ]

    def get_news(self):
        """Return a list of all currently available News items

        @returns {Array.<twitter_bot.model.news_bite.NewsBite>}
        """
        news = []
        for api_service in self.news_services:
            news.extend(api_service.get_news_bites())
        return news
