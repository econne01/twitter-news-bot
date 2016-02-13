"""This is the main function of twitter-news-bot project

It is intended to be run as a cronjob to periodically scan
for news of interest and Tweet about it
"""
import argparse

from twitter_bot.bot import Bot


def _get_command_args():
    parser = argparse.ArgumentParser(description='''
        Command for Twitter Bot to scan news sources, find an interesting
        piece of news and tweet about it
    ''')
    parser.add_argument('--debug', action='store_true')
    return parser.parse_args()

def main():
    command_args = _get_command_args()

    bot = Bot(debug=command_args.debug)
    bot.post_interesting_news()


if __name__ == '__main__':
    main()
