import tkinter as tk
from tkinter import messagebox
import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        
        temperature = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        description = weather['description']
        
        weather_report = (f"City: {city}\n"
                          f"Temperature: {temperature}°C\n"
                          f"Pressure: {pressure} hPa\n"
                          f"Humidity: {humidity}%\n"
                          f"Weather: {description}")
        
        return weather_report
    else:
        return None

def show_weather():
    city = city_entry.get()
    api_key = "YOUR_API_KEY"
    weather = get_weather(city, api_key)
