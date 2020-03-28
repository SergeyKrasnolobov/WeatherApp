from data import get_weather
import os
import requests
import tkinter as tk


HEIGHT = 500
WEIGHT = 500

root = tk.Tk()

API_KEY = "8b9fcf376412413f967f262d0156f9c3"
URL = "http://api.weatherbit.io/v2.0/current"


def weather_description(weather):
    city = weather["data"][0]["city_name"]
    wind_speed = weather["data"][0]["wind_spd"]
    description = weather["data"][0]["weather"]["description"]
    temperature = weather["data"][0]["temp"]

    str = "Город: %s \nСкорость ветра: %s (м/с) \nОписание погоды: %s \nТемпература: %s градусов" % (city, wind_speed, description, temperature)
    return str

def get_weather(city):
    params = {"city": city, "key": API_KEY, "lang": "RU"}
    try:
        response = requests.get(url = URL, params = params)
        data = response.json()
    except:
        print("Что-то пошло не так :(")

    label['text'] = weather_description(data)

canvas = tk.Canvas(root, height = HEIGHT, width = WEIGHT)

canvas.pack()

background_image = tk.PhotoImage(file = os.path.abspath("land.png"))
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg = 'lightblue', bd = 5)
frame.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')

entry = tk.Entry(frame, font = 35)
entry.place(relwidth = 0.65, relheight = 1)

new_button = tk.Button(frame, text = 'Show weather!', bd = 1.25, command = lambda: get_weather(entry.get()))
new_button.place(relx=0.7, relwidth = 0.3, relheight = 1)

lower_frame = tk.Frame(root, bg = 'lightblue', bd = 5)
lower_frame.place(relx = 0.5, rely = 0.25, relwidth=0.75, relheight = 0.6, anchor = 'n')

label = tk.Label(lower_frame, font=('Courier', 11), justify ='center', bd=4)
label.place(relheight=1, relwidth=1)

root.mainloop()
