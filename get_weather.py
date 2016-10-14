# coding: UTF-8

import key
import json
import urllib.request

import get_weather_status

Kelvin_degree = 273.15

api_key = key.WK
api_url = "http://api.openweathermap.org/data/2.5/weather"
city = "Shiga,jp"

req = api_url + "?q=" + city + "&APPID=" + api_key

response = urllib.request.urlopen(req)

data = response.read().decode('utf-8')
json_data = json.loads(data)
weather_data = json_data['weather'][0]
main_data = json_data['main']

def get_status():
    weather_staus_id = weather_data['id']
    weather_status = get_weather_status.get(id)
    return weather_status

def get_icon():
    weather_icon_id = weather_data['icon']
    icon_url = "http://openweathermap.org/img/w/" + str(weather_icon_id) + ".png"
    return icon_url

def get_temp():
    return int(main_data['temp']-Kelvin_degree)

def get_temp_min():
    return int(main_data['temp_min']-Kelvin_degree)

def get_temp_max():
    return int(main_data['temp_max']-Kelvin_degree)

def get_humidity():
    return main_data['humidity']


