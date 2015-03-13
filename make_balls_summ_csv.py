from pandas import *
import numpy as np
import csv

file = open("balls_summ.csv", "w")
out = csv.writer(file, delimiter=',', quoting=csv.QUOTE_NONE)
out.writerow(["ball_summ"])

lottery = np.genfromtxt("MSL.csv", delimiter=",", dtype=np.int32, skip_header=1)

ball_summs_list =[]

for i in range(0, lottery.shape[0]):
    ball_summ = 0
    for ii in range(4, 10):
        ball_summ += lottery[i, ii]
    ball_summs_list.append([ball_summ])

for s in ball_summs_list:
    out.writerow(s)

file.close()






# if ball_summs_list[0] == 5+6+14+15+25+34 and ball_summs_list[8] == 3+8+18+19+21+38:
#     print("TEST OK")
# else:
#     print("PROBLEM")



