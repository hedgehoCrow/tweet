# coding: UTF-8

import key
import json
import urllib.request

import get_weather_status

api_key = key.WK
api_url = "http://api.openweathermap.org/data/2.5/weather"
place = "Tokyo,jp"

req = api_url + "?q=" + place + "&APPID=" + api_key

response = urllib.request.urlopen(req)

data = response.read().decode('utf-8')
json_data = json.loads(data)

weather_staus_id = json_data['weather'][0]['id']
weather_status = get_weather_status.get(id)

print (weather_status)

