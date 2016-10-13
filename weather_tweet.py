# coding: UTF-8

import key
from requests_oauthlib import OAuth1Session
import json

import get_weather

twitter = OAuth1Session(key.CK, key.CS, key.AK, key.AS)

params = {"status": "test\n滋賀の天気は" + get_weather.get_status() + "です"}
req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)
