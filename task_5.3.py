import requests
from pprint import pprint

token = "a97b2f863a8f4aba9461db95c8cc6077"

x = input("Введите название компании:")

def get_sit():
    r = requests.get(
        f"https://newsapi.org/v2/everything?q={x}&from=2022-11-27&to=2022-11-27&sortBy=popularity&apiKey={token}")
    data = r.json()
    # pprint(data)
    count = data['totalResults']
    if count > 0:
        print(f"Найдено {count} статей, выпущенных за вчерашний день, сколько вы хотите увидеть?")
        count = int(input())
        for i in range(0, count):
            author = data['articles'][i]['author']
            description = data['articles'][i]['description']
            print(f"Автор статьи:{author}\n"
                  f"Описание статьи:{description}")
    else:
        print("Не удалось найти статьи с упоминанием компании.")

get_sit()