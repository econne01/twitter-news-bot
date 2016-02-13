"""Service to curate input to determine if it is "interesting" enough to tweet"""

class Curator(object):

    INTERESTING_THRESHOLD = 0.5

    INTERESTING_KEYWORDS = [
        'artificial',
        'brain',
        'education',
        'intelligence',
        'interesting',
        'learning',
        'lifetime',
        'neuroscience',
        'phillies',
        'robot',
        'science',
        'software',
        'twitter'
    ]

    def keep_interesting_items(self, news_bites):
        """Read a list of items and return only the interesting ones

        @param {Array.<twitter_bot.model.news_bite.NewsBite>} news_bites
        @returns {Array.<twitter_bot.model.news_bite.NewsBite>}
        """
        interesting_items = []
        for news_bite in news_bites:
            if self._get_interest_score(news_bite) >= self.INTERESTING_THRESHOLD:
                interesting_items.append(news_bite)
        return interesting_items

    def _get_interest_score(self, news_bite):
        interest_score = 0.0
        for keyword in self.INTERESTING_KEYWORDS:
            if not news_bite.headline:
                continue
            if keyword in news_bite.headline.lower():
                interest_score = 1.0
        return interest_score

