import requests
import tkinter as tk
from io import StringIO
import csv

API_KEY = '2c1ef6189dmsh0162d7166efaca0p10973cjsn4f2d2dc52aa9'  # Your API key

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
        display_weather_forecast(weather_data)
    else:
        print("Failed to fetch weather forecast")

def display_weather_forecast(weather_data):
    result_window = tk.Toplevel(root)
    result_window.title("Weather Forecast")

    result_frame = tk.Frame(result_window)
    result_frame.pack(fill='both', expand=True)

    canvas = tk.Canvas(result_frame)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(result_frame, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor='nw')

    # Use CSV reader to parse the response data
    reader = csv.DictReader(StringIO(weather_data))

    # Frame for each day's data with a border
    for row in reader:
        day_frame = tk.Frame(frame, relief=tk.RIDGE, borderwidth=2)
        day_frame.pack(pady=5, padx=10, anchor='w')

        for key, value in row.items():
            param_label = tk.Label(day_frame, text=f"{key}: {value}", font=("Arial", 11))
            param_label.pack(anchor='w')

    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"), width=500, height=400)

    canvas.bind('<Configure>', on_configure)

def on_submit():
    city = city_entry.get()
    get_weather_forecast(city)

root = tk.Tk()
root.title("Weather Forecast")
root.geometry("600x500")  # Set window size

label = tk.Label(root, text="Enter City:", font=("Arial", 14))
label.pack(pady=10)

city_entry = tk.Entry(root, font=("Arial", 12))
city_entry.pack(pady=5)

submit_button = tk.Button(root, text="Get Forecast", command=on_submit, font=("Arial", 12))
submit_button.pack(pady=10)

root.mainloop()
