# coding: UTF-8

import key
import json
import urllib.request

import get_weather_status

api_key = key.WK
api_url = "http://api.openweathermap.org/data/2.5/weather"
city = "Shiga,jp"

req = api_url + "?q=" + city + "&APPID=" + api_key

response = urllib.request.urlopen(req)

data = response.read().decode('utf-8')
json_data = json.loads(data)
weather_data = json_data['weather'][0]

weather_staus_id = weather_data['id']
weather_status = get_weather_status.get(id)

#print (weather_status)

weather_icon_id = weather_data['icon']
#print (weather_icon_id)
icon_url = "http://openweathermap.org/img/w/" + str(weather_icon_id) + ".png"
#print ("icon_url = " + icon_url)

def get_status():
    return weather_status

def get_icon():
    return icon_url


