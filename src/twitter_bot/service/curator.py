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
        'neuroscience',
        'phillies',
        'robot',
        'science',
        'software',
        'twitter'
    ]

    def keep_interesting_items(self, items):
        """Read a list of items and return only the interesting ones

        @param {List of Strings} items
        """
        interesting_items = []
        for item in items:
            if self._get_interest_score(item) >= self.INTERESTING_THRESHOLD:
                interesting_items.append(item)
        return interesting_items

    def _get_interest_score(self, item):
        interest_score = 0.0
        for keyword in self.INTERESTING_KEYWORDS:
            if keyword in item.lower():
                interest_score = 1.0
        return interest_score

