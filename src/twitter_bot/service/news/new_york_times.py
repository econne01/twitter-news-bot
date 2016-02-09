import requests
from twitter_bot.config.api_keys import NEW_YORK_TIMES_API_KEYS as API_KEYS
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

    def get_latest_headlines(self):
        """Return the latest headlines from NYT website

        @return List of Strings
        """
        headlines = []
        for section in ['home']:
            articles = self.get(section, response_format='json')
        return [article[0] for article in articles]

    def get(self, section='home', response_format='json'):
        """Call the NYTimes API for news headlines from given section

        @return {List of tuples (headline String, url String)}
        """
        url = self._create_api_url(section, response_format)
        response = requests.get(url, params = {'api-key': API_KEYS['TOP_STORIES']})
        articles = response.json()['results']
        return [(article['title'], article['url']) for article in articles]

    def _create_api_url(self, section, response_format):
        return '{base}/{section}.{response_format}'.format(
                base=self.BASE_API_URL,
                section=section,
                response_format=response_format)

