import ssl
import datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen

ssl._create_default_https_context = ssl._create_unverified_context

# Формат даты и времени для добавления к имени файла
date_format = '%Y-%m-%d_%H-%M-%S'

# Основной цикл программы
while True:

    # Запрашиваем у пользователя URL-адрес для распарсивания
    url = input("Введите URL-адрес: ")

    # Получаем текущую дату и время и форматируем их в нужном формате
    now = datetime.datetime.now()
    formatted_date = now.strftime(date_format)

    # Формируем имя файла, включающее текущую дату и время
    file_name = f'text_{formatted_date}.txt'

    # Открываем файл для записи
    with open(file_name, 'a') as file:

        # Получаем HTML-код страницы
        html_code = str(urlopen(url).read(), 'utf-8')

        # Создаем BeautifulSoup-объект из HTML-кода
        soup = BeautifulSoup(html_code, 'html.parser')

        # Получаем заголовок статьи
        title = soup.title.text

        # Записываем заголовок в файл
        file.write(title + '\n\n')

        # Получаем текст статьи
        if soup.find('div', class_='text'):
            s = soup.find('div', class_='text').text
        else:
            s = ''

        # Записываем текст статьи в файл
        file.write(s + '\n')

        # Получаем все абзацы статьи
        p = soup.find_all('p')

        # Записываем каждый абзац в файл
        for i in p:
            file.write(i.text + '\n')

        # Добавляем разделитель между статьями
        file.write('\n\n')

    print(f'Файл {file_name} успешно создан.')

    # Запрашиваем у пользователя выбор: продолжить работу или завершить программу
    choice = input("Хотите продолжить работу? (да/нет): ").lower()

    # Реализуем условие завершения программы при выборе пользователя
    if choice == 'нет':
        break