import json
import requests

from twitter_bot.config.api_keys import GOOGLE_API_KEYS


def get_long_url(short_url):
    """Call Google URL Shortener API to return a long (aka, un-shortened) URL"""
    api_key = GOOGLE_API_KEYS['URL_SHORTENER_API_KEY']
    base_url = 'https://www.googleapis.com/urlshortener/v1/url'
    response = requests.get(base_url,
                            params={'key': api_key, 'shortUrl': short_url})
    return response.json()['longUrl']


def get_short_url(long_url):
    """Call Google URL Shortener API to return shortened URL"""
    api_key = GOOGLE_API_KEYS['URL_SHORTENER_API_KEY']
    base_url = 'https://www.googleapis.com/urlshortener/v1/url'
    headers = {'Content-Type':'application/json'}
    post_data = json.dumps({"longUrl": long_url})
    response = requests.post(base_url, params={'key': api_key}, data=post_data, headers=headers)
    return response.json()['id']
