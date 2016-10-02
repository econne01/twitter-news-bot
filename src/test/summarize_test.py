from test.data.news_bites.bilingual_brains_focus import ARTICLE_JSON
from twitter_bot.model.news_bite import NewsBite
from rake import Rake

def _get_rake():
    rake_dir = '/Users/econnelly/projects/personal/twitter-news-bot/summarizer_comps/RAKE-tutorial'
    stop_words_list_filename = rake_dir + '/SmartStoplist.txt'
    return Rake(stop_words_list_filename,
                min_char_length=1,
                max_words_length=2,
                min_keyword_frequency=2)

if __name__ == '__main__':
    print 'RAKE -- Begin testing'
    news_bite = NewsBite(**ARTICLE_JSON)
    rake_object = _get_rake()
    rake_summary = rake_object.run(news_bite.text)
    print rake_summary
    print 'RAKE -- End testing'
