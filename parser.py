import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings()

# Отправляем GET-запрос на сайт
url = "https://omgtu.ru/general_information/faculties/"
response = requests.get(url, verify=False)

def parse_omgtu():
    # Проверяем успешность запроса
    if response.status_code == 200:
        # Парсим HTML-контент
        soup = BeautifulSoup(response.content, "html.parser")

        # Находим все списки на странице
        chest = soup.find_all("ul")

        # Собираем названия факультетов в одну строку
        string = ''
        for item in chest:
            if item.find('p'):
                # Удаляем лишние переносы строк
                string += item.text.strip()
                string = string.replace('\n\n\n\n', '')

        # Записываем названия факультетов в файл с нумерацией
        with open("omgtu_faculties.txt", "w", encoding="utf-8") as f:
            # Перебираем названия факультетов и записываем их с номерами
            for i, faculty in enumerate(string.split('\n'), start=1):
                f.write(f"{i}. {faculty}\n")
    else:
        print("Не удалось получить список факультетов. Код состояния:", response.status_code)










