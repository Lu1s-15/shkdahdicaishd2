import streamlit as st

import requests
import tkinter as tk
from io import StringIO
import csv

API_KEY = 'J2SPFQATVW74M4R2LK9ESDA9W'  # Your API key

def get_weather_forecast(city):
    url = f"https://visual-crossing-weather.p.rapidapi.com/forecast"
    querystring = {
        "aggregateHours": "24",
        "location": city,
        "contentType": "csv",
        "unitGroup": "us",
        "shortColumnNames": "false"
    }

    headers = {
        'X-RapidAPI-Key': API_KEY,
        'X-RapidAPI-Host': "visual-crossing-weather.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        weather_data = response.text
        print(weather_data)
    else:
        print("Failed to fetch weather forecast")
