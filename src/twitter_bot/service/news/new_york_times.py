from twitter_bot.service.news import BaseNewsService


class NewYorkTimesService(BaseNewsService):

    def get_latest_headlines(self):
        """Return the latest headlines from NYT website

        @return List of Strings
        """
        return ['A boring headline',
                'Wow this is an interesting headline!']
