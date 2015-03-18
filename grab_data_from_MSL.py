import urllib.request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import csv

# Для тестирования
print_info = False

first_page_on_site = 471
last_page_on_site = 1415


# получаем данные с сайта
def get_data_from_site_page(number):
    url_string = "http://msl.ua/uk/megalot/draw-result/draw/%s" % str(number)
    try:
        request = urllib.request.urlopen(url_string)
    except HTTPError as e1:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e1.code)

    except URLError as e2:
        print('We failed to reach a server.')
        print('Reason: ', e2.reason)
    else:
        return request


# переводим название месяца из текста в цифр
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


# загружаем данные в Суп и парсим HTML
def parse_msl_data(request_data):
    soup = BeautifulSoup(request_data)
    # Список с данными одного розыграша
    game = []
    # получаем список всех элементов ul с веб страницы нам нужен шестой в этом списке шарики
    # данные будут в виде списка, возможно с одним элементом
    balls_list = soup.find_all("ul")[5].contents
    for ball in balls_list:
        if ball != '\n':
            game.append(ball.string)
    # ищем элементы b веб страницы та в нем супербол
    game.append(soup.find_all("b")[0].string)
    # ищем элементы h2 веб страницы в них номер и дата розиграша
    game_number_date = soup.find_all("h2")
    # соединяем в одну строку текст из всех элементов
    text = "".join(game_number_date[0].findAll(text=True))
    # разбиваем текст по словам по пробелу
    text_list = text.split(" ")
    #вставляем нужные данные
    game.insert(0, text_list[2][1:])
    game.insert(1, text_list[4])
    game.insert(2, month_to_numb(text_list[5][:3]))
    game.insert(3, text_list[6])
    table = soup.find_all("td")
    table_text = []
    for tab in table:
        table_text.append(tab.findAll(text=True))

                   #"MEGA_JACK_POT_WINNERS", "MEGA_JACK_POT_SUMM"
    append_list = [table_text[1][0], table_text[2][0],
                   #"MEGA_PRISE_WINNERS", "MEGA_PRISE_SUMM"
                   table_text[4][0], table_text[5][0],
                   #"5_plus_MegaBall_WINNERS", "5_plus_MegaBall_SUMM"
                   table_text[7][0], table_text[8][0],
                   #"5_Balls_WINNERS", "5_Balls_SUMM"
                   table_text[10][0], table_text[11][0],
                   #"4_plus_MegaBall_WINNERS", "4_plus_MegaBall_SUMM"
                   table_text[13][0], table_text[14][0],
                   #"4_Balls_WINNERS", "4_Balls_SUMM"
                   table_text[16][0], table_text[17][0],
                   #"3_plus_MegaBall_WINNERS", "3_plus_MegaBall_SUMM"
                   table_text[19][0], table_text[20][0],
                   #"3_Balls_WINNERS", "3_Balls_SUMM"
                   table_text[22][0], table_text[23][0]]

    for win_data in append_list:
        win_data_str = win_data.string.replace(" ", "")
        game.append(win_data_str)
    # print(balls)
    return game


# читаем данные из файла
# http://stackoverflow.com/questions/7257763/adding-data-to-a-csv-file-through-python
def read_msl_csv():
    file = open("MSL.csv", "r")
    msl_data = csv.reader(file)
    msl_data_list = []
    for i in msl_data:
        msl_data_list.append(i)
    file.close()
# http://stackoverflow.com/questions/2793324/is-there-a-simple-way-to-delete-a-list-element-by-value-in-python
    # убираем пустые строки [] из файла
    out_list = [x for x in msl_data_list if len(x) != 0]
    return out_list


# получить все данные с сайта МСЛ и переписать файл:
def get_all_data(last_page=last_page_on_site):
    # создаем файл заново
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

    for page_number in range(first_page_on_site, last_page):
        try:
            print(page_number)
            request_data = get_data_from_site_page(page_number)
            row = parse_msl_data(request_data)
            print(row)
            out.writerow(row)
        except:
            print("Нет данных по розиграшу №%s" % page_number)
    file.close()


# Обновить данные
def update_data():
    msl_data = read_msl_csv()
    if print_info:
        print(msl_data)
    last_game_number = int(msl_data[-1][0])
    if last_game_number < first_page_on_site or not last_game_number:
        print("Файл с данными пустой, скачиваю снова ... ")
        get_all_data()
    print("Последний имеющийся номер розиграша - %s" % last_game_number)
    # открываем файл для добавления данных "a"
    file = open("MSL.csv", "a")
    # создаем писалку в файл (quoting=csv.QUOTE_NONE - не ставить кавычки))
    out = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONE)
    for page_number in range(last_game_number + 1, last_game_number + 20):
        try:
            print(page_number)
            request_data = get_data_from_site_page(page_number)
            row = parse_msl_data(request_data)
            if print_info:
                print(row)
            out.writerow(row)
        except:
            print("Нет данных по розиграшу №%s" % page_number)
    file.close()


if __name__ == '__main__':
    print_info = True
    last_page_on_site = 485
    update_data()

