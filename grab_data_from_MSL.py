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
              "super_ball",
              "MEGA_JACK_POT_WINNERS", "MEGA_JACK_POT_SUMM",
              "MEGA_PRISE_WINNERS", "MEGA_PRISE_SUMM",
              "5_plus_MegaBall_WINNERS", "5_plus_MegaBall_SUMM",
              "5_Balls_WINNERS", "5_Balls_SUMM",
              "4_plus_MegaBall_WINNERS", "4_plus_MegaBall_SUMM",
              "4_Balls_WINNERS", "4_Balls_SUMM",
              "3_plus_MegaBall_WINNERS", "3_plus_MegaBall_SUMM",
              "3_Balls_WINNERS", "3_Balls_SUMM"])


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
for page_number in range(1000, 1050):
    print(page_number)
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
        table = soup.find_all("td")
        table_text = []
        for tab in table:
            table_text.append(tab.findAll(text=True))
        append_list = [table_text[1][0], table_text[2][0], #"MEGA_JACK_POT_WINNERS", "MEGA_JACK_POT_SUMM"
                       table_text[4][0], table_text[5][0], #"MEGA_PRISE_WINNERS", "MEGA_PRISE_SUMM"
                       table_text[7][0], table_text[8][0], #"5_plus_MegaBall_WINNERS", "5_plus_MegaBall_SUMM"
                       table_text[10][0], table_text[11][0], #"5_Balls_WINNERS", "5_Balls_SUMM"
                       table_text[13][0], table_text[14][0], #"4_plus_MegaBall_WINNERS", "4_plus_MegaBall_SUMM"
                       table_text[16][0], table_text[17][0], #"4_Balls_WINNERS", "4_Balls_SUMM"
                       table_text[19][0], table_text[20][0], #"3_plus_MegaBall_WINNERS", "3_plus_MegaBall_SUMM"
                       table_text[22][0], table_text[23][0]] #"3_Balls_WINNERS", "3_Balls_SUMM"

        for win_data in append_list:
            win_data_str = win_data.string.replace(" ", "")
            balls.append(win_data_str)
        # print(balls)
        out.writerow(balls)

