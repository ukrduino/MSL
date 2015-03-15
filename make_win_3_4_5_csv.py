#TODO - частота выпадение шаров(рейтинг)
#TODO - частота выпадения выиграшных "3" "4" "5" (рейтинги)
#TODO - частота выпадения сумм шаров(рейтинг)

from pandas import *
import numpy as np
import csv
# https://docs.python.org/3.4/library/itertools.html#itertools.combinations/
from itertools import combinations

# загружаем файл с данными розиграшей
lottery = np.genfromtxt("MSL.csv", delimiter=",", dtype=np.int32)

#1. Все выиграшные шары в одном списке
all_balls = []

#2. Выиграшные комбинации "6"
win_balls_6_comb_list = []

#3. списки комбинаций образованных  из выиграшных "6"
win_balls_5_comb_list = []
win_balls_4_comb_list = []
win_balls_3_comb_list = []

#4. Все суммы выиграшных комбинаций "6"
ball_summs_list = []

# ------------------------------------------------------------------------

#1. Все выиграшные шары в одном списке
for i in range(4, 10):
    ball_1_all = (lottery[1:, i])
    for ii in ball_1_all:
        all_balls.append(ii)

# Файл с рейтингом шаров по количеству выиграшей
win_balls = open("win_balls.csv", "w")
win_balls_out = csv.writer(win_balls, delimiter=',', quoting=csv.QUOTE_NONE)
win_balls_out.writerow(["ball", "win_times"])

# Пишем в файл номер мяча, количество раз его выпадения
for ball in range(1, 43):
    row = [ball, all_balls.count(ball)]
    win_balls_out.writerow(row)

win_balls.close()

# Cортировка файла с рейтингом шаров по количеству выиграшей
win_balls = pandas.read_csv('win_balls.csv', header=0)
descending_win_balls = win_balls.sort(["win_times"], ascending=[False])
descending_win_balls.to_csv('win_balls.csv', index=False)

# ------------------------------------------------------------------------

#2. Выиграшные комбинации "6"
for row in range(1, lottery.shape[0]):
    win_balls_6 = []
    for i in range(4, 10):
        win_balls_6.append((lottery[row, i]))
    win_balls_6_comb_list.append(win_balls_6)


# Файл со списком комбинаций по 6 шаров образованных  из выиграшных "6"
file6 = open("win_balls_6.csv", "w")
out6 = csv.writer(file6, delimiter=',', quoting=csv.QUOTE_NONE)
out6.writerow(["ball_1", "ball_2", "ball_3", "ball_4", "ball_5", "ball_6", "win_times"])

# Пишем в файл комбинацию, количество раз ее выпадения
for comb in win_balls_6_comb_list:
    csv_row = []
    for i in comb:
        csv_row.append(i)
    csv_row.append(win_balls_6_comb_list.count(comb))
    # нужна нормализация
    # csv_row.append(win_balls_3_comb_list.count(comb)/len(win_balls_3_comb_list * 100))]
    out6.writerow(csv_row)


file6.close()

# Сортировка комбинаций из 6 шаров по частоте выпадения
win_balls_6 = pandas.read_csv('win_balls_6.csv', header=0)
descending_win_balls_6 = win_balls_6.sort(["win_times"], ascending=[False])
descending_win_balls_6.to_csv('win_balls_6.csv', index=False)

# ------------------------------------------------------------------------
#3. списки комбинаций образованных  из выиграшных "6"

# Список комбинаций по 5 шаров образованных  из выиграшных "6"
for comb in win_balls_6_comb_list:
    win_5_balls_combinations = combinations(comb, 5)
    for win_5_balls_combination in win_5_balls_combinations:
        win_5_balls_lst = []
        for ball in win_5_balls_combination:
            win_5_balls_lst.append(ball)
        win_balls_5_comb_list.append(win_5_balls_lst)


# Файл со списком комбинаций по 5 шара образованных  из выиграшных "6"
file5 = open("win_balls_5.csv", "w")
out5 = csv.writer(file5, delimiter=',', quoting=csv.QUOTE_NONE)
out5.writerow(["ball_1", "ball_2", "ball_3", "ball_4", "ball_5", "win_times"])

# Пишем в файл комбинацию, количество раз ее выпадения
for comb in win_balls_5_comb_list:
    csv_row = []
    for i in comb:
        csv_row.append(i)
    csv_row.append(win_balls_5_comb_list.count(comb))
    # нужна нормализация
    # csv_row.append(win_balls_3_comb_list.count(comb)/len(win_balls_3_comb_list * 100))]
    out5.writerow(csv_row)

file5.close()

# Сортировка комбинаций из 5 шаров по частоте выпадения
win_balls_5 = pandas.read_csv('win_balls_5.csv', header=0)
descending_win_balls_5 = win_balls_5.sort(["win_times"], ascending=[False])
descending_win_balls_5.to_csv('win_balls_5.csv', index=False)

# ------------------------
# Список комбинаций по 4 шара образованных  из выиграшных "6"
for comb in win_balls_6_comb_list:
    win_4_balls_combinations = combinations(comb, 4)
    for win_4_balls_combination in win_4_balls_combinations:
        win_4_balls_lst = []
        for ball in win_4_balls_combination:
            win_4_balls_lst.append(ball)
        win_balls_4_comb_list.append(win_4_balls_lst)


# Файл со списком комбинаций по 4 шара образованных  из выиграшных "6"
file4 = open("win_balls_4.csv", "w")
out4 = csv.writer(file4, delimiter=',', quoting=csv.QUOTE_NONE)
out4.writerow(["ball_1", "ball_2", "ball_3", "ball_4", "win_times"])

# Пишем в файл комбинацию, количество раз ее выпадения
for comb in win_balls_4_comb_list:
    csv_row = []
    for i in comb:
        csv_row.append(i)
    csv_row.append(win_balls_4_comb_list.count(comb))
    # нужна нормализация
    # csv_row.append(win_balls_3_comb_list.count(comb)/len(win_balls_3_comb_list * 100))]
    out4.writerow(csv_row)

file4.close()

# Сортировка комбинаций из 5 шаров по частоте выпадения
win_balls_4 = pandas.read_csv('win_balls_4.csv', header=0)
descending_win_balls_4 = win_balls_4.sort(["win_times"], ascending=[False])
descending_win_balls_4.to_csv('win_balls_4.csv', index=False)

# ------------------------
# Список комбинаций по 3 шара образованных  из выиграшных "6"
for comb in win_balls_6_comb_list:
    win_3_balls_combinations = combinations(comb, 3)
    for win_3_balls_combination in win_3_balls_combinations:
        win_3_balls_lst = []
        for ball in win_3_balls_combination:
            win_3_balls_lst.append(ball)
        win_balls_3_comb_list.append(win_3_balls_lst)


# Файл со списком комбинаций по 3 шара образованных  из выиграшных "6"
file3 = open("win_balls_3.csv", "w")
out3 = csv.writer(file3, delimiter=',', quoting=csv.QUOTE_NONE)
out3.writerow(["ball_1", "ball_2", "ball_3", "win_times"])

# Пишем в файл комбинацию, количество раз ее выпадения
for comb in win_balls_3_comb_list:
    csv_row = []
    for i in comb:
        csv_row.append(i)
    csv_row.append(win_balls_3_comb_list.count(comb))
    # нужна нормализация
    # csv_row.append(win_balls_3_comb_list.count(comb)/len(win_balls_3_comb_list * 100))]
    out3.writerow(csv_row)

file3.close()

# Сортировка комбинаций из 5 шаров по частоте выпадения
win_balls_3 = pandas.read_csv('win_balls_3.csv', header=0)
descending_win_balls_3 = win_balls_3.sort(["win_times"], ascending=[False])
descending_win_balls_3.to_csv('win_balls_3.csv', index=False)

# ------------------------------------------------------------------------

#4. Все суммы выиграшных комбинаций "6"

# Список всех сумм выиграшных комбинаций "6"
for i in range(1, lottery.shape[0]):
    ball_summ = 0
    for ii in range(4, 10):
        ball_summ += lottery[i, ii]
    ball_summs_list.append(ball_summ)

# Файл со списком сумм выиграшных комбинаций "6"
balls_summ = open("win_balls_summs.csv", "w")
summ_out = csv.writer(balls_summ, delimiter=',', quoting=csv.QUOTE_NONE)
summ_out.writerow(["win_balls_summ", "win_times"])


# Пишем в файл сумму, количество выиграшей
for comb in ball_summs_list:
    csv_row = [comb, ball_summs_list.count(comb)]
    summ_out.writerow(csv_row)

balls_summ.close()


# Сортировка сумм выиграшных "6" по частоте выпадения  и удаляем дубликаты
ball_summs = pandas.read_csv('win_balls_summs.csv', header=0)
unique_ball_summs = ball_summs.drop_duplicates()
descending_ball_summs = unique_ball_summs.sort(["win_times"], ascending=[False])
descending_ball_summs.to_csv('win_balls_summs.csv', index=False)