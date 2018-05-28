import re
import time
import requests

from twitter_bot.config.api_keys import NEW_YORK_TIMES_API_KEYS as API_KEYS
from twitter_bot.model.news_bite import NewsBite
from twitter_bot.service.news import BaseNewsService


SECTIONS = [
    'home',
    'world',
    'politics',
    'nyregion',
    'business',
    'technology',
    'science',
    'health'
]


class NewYorkTimesService(BaseNewsService):

    BASE_API_URL = 'http://api.nytimes.com/svc/topstories/v1'

    def get_news_bites(self):
        """Return the latest news items from NYT website

        @returns {Array.<twitter_bot.model.news_bite.NewsBite>}
        """
        news_bites = []
        for section in SECTIONS:
            news_bites += self._get_section_news(section)
            time.sleep(1)  # Sleep 1 second so we don't exceed API rate of 5 calls per second
        return news_bites

    def _convert_json_to_news_bite(self, nyt_article):
        """Convert a JSON object (from NYT API response) to NewsBite"""
        return NewsBite(
            url=nyt_article['url'],
            # (?i) denotes case-insensitive matching
            author=re.sub('(?i)^by ', '', nyt_article['byline']),
            category=nyt_article['section'],
            headline=nyt_article['title'],
            publish_date=nyt_article['published_date'],
            synopsis=nyt_article['abstract']
        )

    def _create_api_url(self, section, response_format):
        return '{base}/{section}.{response_format}'.format(
                base=self.BASE_API_URL,
                section=section,
                response_format=response_format)

    def _get_section_news(self, section):
        """Call the NYTimes API for news headlines from given section

        @returns {Array.<twitter_bot.model.news_bite.NewsBite>}
        """
        url = self._create_api_url(section, 'json')
        response = requests.get(url, params = {'api-key': API_KEYS['TOP_STORIES']})
        response_json = response.json()
        try:
            articles = response_json['results']
        except KeyError as exc:
            print(exc)
            print(response.json())
        return [self._convert_json_to_news_bite(article) for article in articles]

