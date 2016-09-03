# -*- coding: utf-8 -*-
import twitter
import json

# ตั้ง API ตรงนี้นะครับ
api = twitter.Api(consumer_key="",
    consumer_secret="",
    access_token_key="",
    access_token_secret="")

wordList = ["แล้ว","แย้ว","แบ้ว","ล้าว"]
listLength = len(wordList)
countList = [0] * listLength
sumWordList = ""

for i in range(0,listLength):
    sumWordList += "_{}".format(wordList[i])

f = open("TweetList{}.txt".format(sumWordList), 'w+')
lines = f.readlines()
for line in lines:
    f.write("")

for i in range(0,listLength):
    print("===================================\n{}\n===================================".format(wordList[i]))
    f.write("===================================\n{}\n===================================\n".format(wordList[i]))
    resultsList = api.GetSearch(raw_query="q=" + wordList[i] + "%20AND%20-filter%3Aretweets%20lang%3Ath&src=typd&count=100&result_type=recent")

    for results in resultsList:
        tweetText = results.user.screen_name + ": " + results.text
        print(tweetText)
        f.write(tweetText.encode('utf-8')+"\n")
        countList[i]+=1

print("\n\n==========\nสรุปสถิติ\n==========")
f.write("\n\n==========\nสรุปสถิติ\n==========\n")
for i in range(0,listLength):
    print("{}: {}".format(wordList[i],countList[i]))
    f.write("{}: {}\n".format(wordList[i],countList[i]))
