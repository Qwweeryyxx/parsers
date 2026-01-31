from config import user
import requests
from bs4 import BeautifulSoup

text = input("введите поисковый запрос: ")
search = text.replace(" ", "+")

url = f"https://yandex.ru/search/?text={search}"

code = requests.get(url, headers=user)
soup = BeautifulSoup(code.text, "html.parser")


#bot.send_message(-1003548428518, "Hello, this is a test message!")