
# FIFTH SECTION
# 21 Question
class FileManager:

    def write(self,text):
        with open("something1.txt","a") as file:
            file.write(text)

    def read(self):
        with open("something1.txt","r") as file:
            return file.read()

# 22 Question
import datetime

class Log:
    def __init__(self,file):
        self.file = file

    def write_message(self,error_message):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.file,'a') as file:
            file.write(f'[{timestamp}] ERROR: {error_message}:\n')

log = Log('app.log')
log.write_message("This is an error Message")

# 25 Question
class Report:

    def __init__(self,file):
        self.file = file

    def generate_report(self):
        try:
            with open(self.file,'r') as file:
                data = file.read()
                print("Report generated successfully.")
                if data:
                    return data
                else:
                    return 'Nothing inside the file.'
        except FileNotFoundError:
            print("Error: No such file found in the directory.")
        except IOError as e:
            print("Error",e)

r = Report('something1.txt')
print(r.generate_report())

import tkinter as tk
from tkinter import ttk, messagebox
import requests

class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Weather App")
        self.geometry("400x300")

        # API key for OpenWeatherMap
        self.api_key = "your_api_key_here"  # Replace with your actual API key

        # Create a label and entry for city name
        self.city_label = ttk.Label(self, text="Enter City Name:")
        self.city_label.pack(pady=10)

        self.city_entry = ttk.Entry(self)
        self.city_entry.pack(pady=5)

        # Create a button to fetch weather
        self.fetch_button = ttk.Button(self, text="Get Weather", command=self.get_weather)
        self.fetch_button.pack(pady=10)

        # Frame for displaying weather results
        self.result_frame = ttk.Frame(self)
        self.result_frame.pack(pady=20)

        self.weather_result = tk.StringVar()
        self.result_label = ttk.Label(self.result_frame, textvariable=self.weather_result, wraplength=300, justify="left")
        self.result_label.pack()

    def get_weather(self):
        city_name = self.city_entry.get()
        if not city_name:
            messagebox.showwarning("Input Error", "Please enter a city name.")
            return

        # Fetch weather data
        weather_data = self.fetch_weather_data(city_name)
        if weather_data:
            self.display_weather(weather_data)

    def fetch_weather_data(self, city_name):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={self.api_key}&units=metric"
        try:
            response = requests.get(url)
            data = response.json()
            if data["cod"] != 200:
                messagebox.showerror("Error", data["message"])
                return None
            return data
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", "Failed to connect to the weather service.")
            return None

    def display_weather(self, weather_data):
        city = weather_data["name"]
        country = weather_data["sys"]["country"]
        temp = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        weather_info = (
            f"City: {city}, {country}\n"
            f"Temperature: {temp}°C\n"
            f"Condition: {description.capitalize()}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
        )
        self.weather_result.set(weather_info)

if __name__ == "__main__":
    app = WeatherApp()
    app.mainloop()
