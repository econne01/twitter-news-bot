# twitter-news-bot
Source code for a Twitter Bot to curate news content and tweet about what it "considers" interesting
The bot is currently tweeting with username [@OMG_News_Bot](https://twitter.com/OMG_News_Bot)

## Setup and Installation
Simple!
```
git clone git@github.com:econne01/twitter-news-bot.git
python src/setup.py
```

## Running
Twitter News Bot provides one main python script that can be run to trigger the full process of
1. Scanning news sources
2. Identifying "interesting" articles
3. Posting an article to Twitter

## Deploying
Twitter news bot is deployed to an AWS EC2 instance. As described in the Setup section, there are very little
requirements.
The only real step to deploy is to set up a cron job to periodically run this python script.
