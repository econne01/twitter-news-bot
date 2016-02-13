"""Model representing an individual piece of news content from internet"""


class NewsBite(object):

    def __init__(self, url, author=None, category=None, headline=None,
                 publish_date=None, synopsis=None):
        self.url = url
        if author:
            self.author = author
        if category:
            self.category = category
        if headline:
            self.headline = headline
        if publish_date:
            self.publish_date = publish_date
        if synopsis:
            self.synopsis = synopsis
        self.tags = []

