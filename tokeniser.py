# -*- coding: utf-8 -*-
import tweepy
import webbrowser

consumer_key = ""
consumer_secret = ""

if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    webbrowser.open(auth.get_authorization_url())
    pin = raw_input('Verification pin number from twitter.com: ').strip()
    token = auth.get_access_token(verifier=pin)

    print token
