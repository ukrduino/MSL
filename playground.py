import csv

print_info = False

test_row = ["game_number", "day", "month", "year", "ball_1", "ball_2", "ball_3", "ball_4", "ball_5", "ball_6",
                  "super_ball",
                  "MEGA_JACK_POT_WINNERS", "MEGA_JACK_POT_SUMM",
                  "MEGA_PRISE_WINNERS", "MEGA_PRISE_SUMM",
                  "5_plus_MegaBall_WINNERS", "5_plus_MegaBall_SUMM",
                  "5_Balls_WINNERS", "5_Balls_SUMM",
                  "4_plus_MegaBall_WINNERS", "4_plus_MegaBall_SUMM",
                  "4_Balls_WINNERS", "4_Balls_SUMM",
                  "3_plus_MegaBall_WINNERS", "3_plus_MegaBall_SUMM",
                  "3_Balls_WINNERS", "3_Balls_SUMM"]


def append_to_csv(row):
    # открываем файл для дозаписи "а"
    file = open("MSL.csv", "a")
    # создаем писалку в файл (quoting=csv.QUOTE_NONE - не ставить кавычки))
    out = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONE)
    # пишем в конец файла
    out.writerow(row)


# http://stackoverflow.com/questions/7257763/adding-data-to-a-csv-file-through-python
def read_csv(start_line=None, end_line=None):
    file = open("MSL.csv", "r")
    msl_data = csv.reader(file)
    msl_data_list = []
    for i in msl_data:
        msl_data_list.append(i)
    try:
        if start_line and not end_line:
            if len(msl_data_list) > start_line > len(msl_data_list) * -1:
                if print_info:
                    print("Строка №%s" % start_line)
                    print(msl_data_list[start_line])
                return msl_data_list[start_line]
        elif start_line and end_line:
            if len(msl_data_list) > start_line > len(msl_data_list) * -1:
                if len(msl_data_list) > start_line > len(msl_data_list) * -1:
                    if print_info:
                        print("Диапазон со стр №%s до стр №%s" % (start_line, end_line))
                    return msl_data_list[start_line:end_line]

        else:
            if print_info:
                print("Нет такой строки, получите весь список!")
            return msl_data_list
    except:
        print("Не могу!")
        return None


        # def friend_exists(friend):
        #     reader = csv.reader(open("friends.csv", "rb"), delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        #     for row in reader:
        #         if (row == friend):
        #             return True
        #     return False
        #


if __name__ == '__main__':
    print_info = True
a = read_csv(start_line=1, end_line=3)
b = read_csv(0,3)
c = read_csv("t")
d = read_csv(-1)
print(a)
print(b)
print(c)
print(d)