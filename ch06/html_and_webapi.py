# -*- coding: utf-8 -*-
import json
import os
import urllib
import urlparse
from requests.auth import OAuth1
import requests
import twitter
from study import p
import study
from pandas import DataFrame

def main():
    '''
    HTML and WebAPI
    '''
    twitter_secret_path = study.ROOT_DIR + '/twitter_secret.json'
    with open(twitter_secret_path) as f:
        tw_secret = json.load(f)
        p(tw_secret)

    format_tweets(search_tweets(tw_secret))
    format_tweets(search_and_post_status(tw_secret))

def search_tweets(tw_secret):
    '''
    Using twitter module
    '''
    MY_TWITTER_CREDS = os.path.expanduser(study.ROOT_DIR + '/.my_app_credentials')
    CONSUMER_KEY = tw_secret['api_key']
    CONSUMER_SECRET = tw_secret['api_secret_key']

    if not os.path.exists(MY_TWITTER_CREDS):
        twitter.oauth_dance('My App Name', CONSUMER_KEY, CONSUMER_SECRET, MY_TWITTER_CREDS)

    # oauth_token is access_token format
    # oauth_secret is access_token_secret format
    oauth_token, oauth_secret = twitter.read_token_file(MY_TWITTER_CREDS)
    p(oauth_token)
    p(oauth_secret)

    auth = twitter.OAuth(oauth_token, oauth_secret, CONSUMER_KEY, CONSUMER_SECRET)
    t = twitter.Twitter(auth=auth)
    q = urllib.quote('python pandas')
    p(q)

    return t.search.tweets(q=q)

def format_tweets(data):
    p(data.keys())
    p(data['search_metadata'])
    p(data['statuses'][0].keys())
    tweet_fields = ['created_at', 'from_user', 'id', 'text']
    tweets = DataFrame(data['statuses'], columns=tweet_fields)
    p(tweets)
    p(tweets.ix[7])

def search_and_post_status(tw_secret):
    """
    oauth by requests module
    """
    CONSUMER_KEY = tw_secret['api_key']
    CONSUMER_SECRET = tw_secret['api_secret_key']
    # request token
    request_token_url = 'https://api.twitter.com/oauth/request_token'
    auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET, callback_uri=u'oob')
    res = requests.post(request_token_url, auth=auth)
    request_token = dict(urlparse.parse_qsl(res.text))
    p(request_token)

    # access token
    authorize_url = 'https://api.twitter.com/oauth/authorize'
    access_token_url = 'https://api.twitter.com/oauth/access_token'
    # Authorize
    print 'Auth link:'
    print '{0}?oauth_token={1}'.format(authorize_url, request_token['oauth_token'])
    print
    oauth_verifier = unicode(raw_input('What is the PIN? '))
    auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET,
                  request_token['oauth_token'], request_token['oauth_token_secret'],
                  verifier=oauth_verifier)
    res = requests.post(access_token_url, auth=auth)
    access_token = dict(urlparse.parse_qsl(res.text))
    p(access_token)

    # search
    search_url = 'https://api.twitter.com/1.1/search/tweets.json'
    query = urllib.quote('python pandas')
    auth = OAuth1(CONSUMER_KEY, CONSUMER_SECRET,
                  access_token['oauth_token'], access_token['oauth_token_secret'])
    res = requests.get(search_url + '?q=' + query, auth=auth)
    tweets = json.loads(res.text)
    format_tweets(tweets)

    # post status
    update_url = 'https://api.twitter.com/1.1/statuses/update.json'
    data = {
        'status': 'This status is posted by requests module.',
    }
    res = requests.post(update_url, data=data, auth=auth)
    p(res.text)

if __name__ == '__main__':
    main()
