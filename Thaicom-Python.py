# -*- coding: utf-8 -*-
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

access_token = "32888622-HwU7SenhVn9cjcIHSFH2WAXp6WYRlO2UBq27XEOqp"
access_token_secret = "ScAWnFjlLquKjVYZSpM3hoHqnZJqgv6wtHMyXURYkUmyI"
consumer_key = "w9UEbrHRrOGvVIy5tWcvWWPlJ"
consumer_secret = "nGLFkPcJD1w0u4MlnucrW3iHk1jolpjfUk2I36VQkyA1ABkQjL"

wordList = [u'นะค่ะ', u'เซง', u'น่ะคะ', u'น๊คร๊', u'ฝันเด', u'ควัย']

f = open('badList.txt','w');

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        parseddata = json.loads(data)
        for word in wordList:
            if parseddata[u'text'].find(word) > -1:
                f.write(parseddata[u'user'][u'screen_name'] + ": " + parseddata[u'text'] + "\n")
                print parseddata[u'user'][u'screen_name'] + ": " + parseddata[u'text']
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    print "Streaming!"

    stream.filter(locations=[100.210824,13.528408,100.945534,14.230996])
