import requests
from pprint import pprint


def get_weather(city, token):
    r = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric")
    data = r.json()
    # pprint(data)
    city_ = data['name']

    temp = data['main']['temp']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    print(f"Погода в городе: {city_}\n"
          f"Температура: {temp}\n"
          f"Влажность: {humidity}%\n"
          f"Давление: {pressure}")


token = "ab5409a766315ed0eec359867e62ac6a"
city = input("Введите название города:")
get_weather(city, token)