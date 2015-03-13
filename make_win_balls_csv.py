#TODO - частота выпадение шаров
# http://stackoverflow.com/questions/18204134/install-python-numpy-in-the-virtualenv-environment
from pandas import *
import numpy as np
import csv


lottery = np.genfromtxt("MSL.csv", delimiter=",", dtype=np.int32, skip_header=1)

all_balls = []

for i in range(4, 10):
    ball_1_all = (lottery[:, i])
    for ii in ball_1_all:
        all_balls.append(ii)


file = open("win_balls.csv", "w")
out = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONE)
out.writerow(["ball", "win_times"])

for iii in range(1, 43):
    pair = [iii, all_balls.count(iii)]
    out.writerow(pair)

file.close()


win_balls = pandas.read_csv('win_balls.csv', header=0)
descending_win_balls = win_balls.sort(["win_times"], ascending=[False])
descending_win_balls["perc"] = descending_win_balls["win_times"] / 109 * 100
descending_win_balls["perc"] = descending_win_balls["perc"].astype(int)
descending_win_balls.to_csv('win_balls.csv', index=False)

print(descending_win_balls)


# pd.options.display.float_format = '{:,.0f}'.format