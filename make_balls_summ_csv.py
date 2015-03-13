#TODO - частота выпадения сумм шаров
from pandas import *
import numpy as np
import csv

file = open("balls_summ.csv", "w")
out = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONE)
out.writerow(["ball_summ", "win_times"])

lottery = np.genfromtxt("MSL.csv", delimiter=",", dtype=np.int, skip_header=1)

ball_summs_list =[]
ball_summs_rating_dict ={}


for i in range(0, lottery.shape[0]):
    ball_summ = 0
    for ii in range(4, 10):
        ball_summ += lottery[i, ii]
    ball_summs_list.append(ball_summ)


for summ in ball_summs_list:
    if summ in ball_summs_rating_dict:
        ball_summs_rating_dict[summ] += 1
    else:
        ball_summs_rating_dict[summ] = 1

print(ball_summs_rating_dict)

for k, v in ball_summs_rating_dict.items():
    pair = [k, v]
    out.writerow(pair)

file.close()

ball_summs = pandas.read_csv('balls_summ.csv', header=0)
descending_win_balls = ball_summs.sort(["win_times"], ascending=[False])
descending_win_balls["perc"] = descending_win_balls["win_times"] / descending_win_balls.size * 100
descending_win_balls["perc"] = descending_win_balls["perc"].astype(int)
print(descending_win_balls)
descending_win_balls.to_csv('balls_summ.csv', index=False)





# if ball_summs_list[0] == 5+6+14+15+25+34 and ball_summs_list[8] == 3+8+18+19+21+38:
#     print("TEST OK")
# else:
#     print("PROBLEM")



