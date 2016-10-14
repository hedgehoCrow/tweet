# coding: UTF-8

import key
from requests_oauthlib import OAuth1Session
import json

from get_weather import *

twitter = OAuth1Session(key.CK, key.CS, key.AK, key.AS)

status = get_status()
temp = str(get_temp())
temp_max = str(get_temp_max())
temp_min = str(get_temp_min())
humidity = str(get_humidity())

params = {"status": "test\n滋賀の天気は" + status + "です\n" + "現在の気温は" + temp + "度\n" + "湿度は" + humidity + "です\n"}
#params = {"status": "test\n滋賀の天気は" + status + "です\n" + "現在の気温は" + temp + "度\n" + "今日の最高気温は" + temp_max + "度\n" + "今日の最低気温は" + temp_min + "度です\n"}
req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)
