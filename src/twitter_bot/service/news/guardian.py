from datetime import date, timedelta
import requests
import urllib

from twitter_bot.config.api_keys import GUARDIAN_API_KEY
from twitter_bot.model.news_bite import NewsBite
from twitter_bot.service.news import BaseNewsService


SECTIONS = [
    'books',
    'business',
    'commentisfree',  # Opinion Section
    'culture',
    'education',
    'environment',
    'global-development',
    'money',
    'science',
    'society',
    'technology',
    'world'
]


class GuardianService(BaseNewsService):

    BASE_API_URL = 'http://content.guardianapis.com/search'

    def get_news_bites(self):
        """Return the latest news items

        @returns {Array.<twitter_bot.model.news_bite.NewsBite>}
        """
        news_bites = []
        for section in SECTIONS:
            news_bites += self._get_section_news(section)
        return news_bites

    def _convert_json_to_news_bite(self, news_item):
        """Convert a JSON object (from NYT API response) to NewsBite"""
        return NewsBite(
            url=news_item['webUrl'],
            category=news_item['sectionName'],
            headline=news_item['webTitle'],
            publish_date=news_item['webPublicationDate']
        )

    def _get_all_page_results(self, api_url, page_size=100):
        """Page through all available results and aggregate API results, then return

        @param {string} api_url - the main API url from which to make paged calls
        @param {integer} page_size - number of results per page
        @returns {Array.{json}}
        """
        page = 1
        results = []
        total_result_count = None
        while (total_result_count is None or page * page_size < total_result_count):
            response = requests.get(api_url, params={
                'page-size': page_size,
                'page': page
            })
            response_json = response.json()['response']
            if response_json['status'] == 'error':
                break

            if total_result_count is None:
                total_result_count = response_json['total']

            results += response_json['results']
            page += 1
        return results

    def _get_recent_news(self, since_days=1, section=None):
        """Call the Guardian API for recent news items (articles only)

        @param {integer} since_days - how many days to set filter limit for "recent"
        @returns {Array.<twitter_bot.model.news_bite.NewsBite>}
        """
        params = {
            'api-key': GUARDIAN_API_KEY,
            'from-date': (date.today() - timedelta(days=since_days)).strftime('%Y-%m-%d'),
            'order-by': 'newest',
            'type': 'article'
        }
        if section:
            params['section'] = section
        api_url = self.BASE_API_URL + '?{params}'.format(params=urllib.urlencode(params))
        articles = self._get_all_page_results(api_url)
        return [self._convert_json_to_news_bite(article) for article in articles]

    def _get_section_news(self, section, since_days=1):
        """Return a list of NewsBites from given section API

        @returns {Array.<twitter_bot.model.news_bite.NewsBite>}
        """
        return self._get_recent_news(since_days=since_days, section=section)

