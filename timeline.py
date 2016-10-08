# coding: UTF-8

import key
from requests_oauthlib import OAuth1Session
import json

twitter = OAuth1Session(key.CK, key.CS, key.AK, key.AS)

params = {}
req = twitter.get("https://api.twitter.com/1.1/statuses/home_timeline.json", params = params)

timeline = json.loads(req.text)

for tweet in timeline:
    print (tweet["text"])

