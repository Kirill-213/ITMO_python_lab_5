import requests
from pprint import pprint


def get_weather(city, token):
    r = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric")
    data = r.json()
    city_name = data['name']

    temp = data['main']['temp']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    print(f"Погода в городе: {city_name}\n"
          f"Температура: {temp}\n"
          f"Влажность: {humidity}%\n"
          f"Давление: {pressure}")


token = "22028da723e72c43546500e68658f105"

city = input("Введите название города:")
get_weather(city, token)