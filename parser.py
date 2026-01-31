import requests
from bs4 import BeautifulSoup

city = input("Enter city name: ")
url = f"https://yandex.ru/pogoda/ru/{city}"

user = {
    "User": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get(url, headers=user)
#print(response)

soup = BeautifulSoup(response.text, "html.parser")

temp = soup.select(".AppFactTemperature_value__2qhsG")[0].get_text()
print(f"Temperature in {city}: {temp}")


