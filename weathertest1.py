import streamlit as st

#put in OpenWeather API: 
#documentation: https://openweathermap.org/current

import requests

class Weather:
    def __init__(self, coordinate_x, coordinate_y, hightemperature, lowtemperature, wind, rain):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coordinate_y
        self.hightemperature = hightemperature
        self.lowtemperature = lowtemperature
        self.wind = wind
        self.rain = rain

    def __str__(self):
        return "High Temperature:{}, Low Temperature:{} Wind:{} Rain:{}".format(self.hightemperature, self.lowtemperature, self.wind, self.rain)

API_KEY = "d63b8eeb0d4b9d5edcd1ba8eefac429e"

def get_weather(x, y):
    api_key = API_KEY
    url = 'https://api.openweathermap.org/data/2.5/weather'

    params = {
        'lat': x,
        'lon': y,
        'appid': api_key,
        'units': 'metric'
    }

    r = requests.get(url, params=params)
    weather = r.json()

    latitude = weather['coord']['lat']
    longitude = weather['coord']['lon']

    main_data = weather.get('main', {})
    hightemperature = main_data.get('temp_max', 0)
    lowtemperature = main_data.get('temp_min', 0)

    wind_data = weather.get('wind', {})
    wind_speed = wind_data.get('speed', 0)
    wind_deg = wind_data.get('deg', 0)

    rain_data = weather.get('rain', {})
    rain = rain_data.get('1h', 0)

    return Weather(latitude, longitude, hightemperature, lowtemperature, wind_speed, rain)

#example for Winterthur:
city_weather = get_weather(44.34, 10.99)
print(city_weather)
#output is then: High Temperature:8.65°C, Low Temperature:4.59°C Wind:0.69m/s Rain:0mm

#use API to transform city names(user input) into coordinates
api_key = 'c83432faad258b25aa25115b10c40917'
#https://openweathermap.org/api/geocoding-api#reverse
def city_to_coordinates(q, appid , limit=1):
    url = 'https://api.openweathermap.org/data/2.5/weather'

    params = {
        'q': q,
        'appid': appid,
    } 

    response = requests.get(url, params=params)   

    if response.status_code == 200:
        data = response.json() 
        if 'coord' in data:  #chagpt: line22-27
            return data['coord']
        else:
            return None
    else:
        return None

#streamlit: get user input
user_input = st.text_input('Enter your current location (city)', '')

#convert user input into coordinates with function city_to_coordinates
if user_input: 
  coordinates = city_to_coordinates(user_input, api_key)

  if coordinates: 
        st.write(f"Coordinates for {user_input}: {coordinates}")
        
        # Use the converted coordinates to get the corresponding weather information
        weather_data = get_weather(coordinates['lat'], coordinates['lon'])
        
        # example to retrieve data 
        st.write(f"High temperature: {weather_data.hightemperature}")
        
        # example for the rest of the code(?) 
        if weather_data.hightemperature > 30:
        		st.write('Wear warm clothes')
  else:
        st.write(f"Coordinates for {user_input} not found")

if not user_input: 
  st.warning('Please enter a city', icon="⚠️") 
#allow location input, also maybe preference for warm clothes or lighter clothes

#display weather chart and prognosis

#display what clothes to wear 