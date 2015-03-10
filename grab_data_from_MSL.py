import urllib.request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import csv

# создаем файл
file = open("MSL.csv", "w")
# создаем писалку в файл (quoting=csv.QUOTE_NONE - не ставить кавычки))
out = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONE)
# пишем заголовочную строку
out.writerow(["game_number", "day", "month", "year", "ball_1", "ball_2", "ball_3", "ball_4", "ball_5", "ball_6",
              "super_ball"])


# получаем данные с сайта
def get_data_from_site(number):
    url_string = "http://msl.ua/uk/megalot/draw-result/draw/%s" % str(number)
    request = urllib.request.urlopen(url_string)
    return request


def month_to_numb(month=None):
    if month == "січ":
        return 1
    elif month == "лют":
        return 2
    elif month == "бер":
        return 3
    elif month == "кві":
        return 4
    elif month == "тра":
        return 5
    elif month == "чер":
        return 6
    elif month == "лип":
        return 7
    elif month == "сер":
        return 8
    elif month == "вер":
        return 9
    elif month == "жов":
        return 10
    elif month == "лис":
        return 11
    elif month == "гру":
        return 12
    else:
        return 0

# обходим все страницы
for page_number in range(471, 1411):
    # если удалось получить данные то переходим вниз
    try:
        request_data = get_data_from_site(page_number)

    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    else:
        # everything is fine
        # загружаем данные в Суп
        soup = BeautifulSoup(request_data)
        # Список с данными одного розыграша
        balls = []
        # получаем список всех элементов ul с веб страницы нам нужен шестой в этом списке шарики
        # данные будут в виде списка, возможно с 1 элементом
        results = soup.find_all("ul")[5].contents
        for ttt in results:
            if ttt != '\n':
                balls.append(ttt.string)
        # ищем элементы b веб страницы та в нем супербол
        balls.append(soup.find_all("b")[0].string)
        # ищем элементы h2 веб страницы в них номер и дата розиграша
        game_number_date = soup.find_all("h2")
        # соединяем в одну строку текст из всех элементов
        text = "".join(game_number_date[0].findAll(text=True))
        # разбиваем текст по словам по пробелу
        text_list = text.split(" ")
        #вставляем нужные данные
        balls.insert(0, text_list[2][1:])
        balls.insert(1, text_list[4])
        balls.insert(2, month_to_numb(text_list[5][:3]))
        balls.insert(3, text_list[6])
        print(balls)
        out.writerow(balls)

