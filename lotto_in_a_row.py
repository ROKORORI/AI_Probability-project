import pandas as pd
import csv

#  연속된 수 나오는 경우의 수 ex) 12, 13 ,14 ,15 등
lotto_in_a_row = [0, 0, 0, 0, 0, 0]

f = open("lotto ~ 1092.csv", 'r')
rdr = csv.reader(f)
lotto_num = []
for line in rdr:
    lotto_num.append(line[1:7])
f.close()
lotto_num.pop(0)

for i in range(len(lotto_num)):
    lotto_num[i] = list(map(int, lotto_num[i]))
    lotto_num[i].sort()

for i in range(1, 6):
    for j in range(len(lotto_num)):
        for k in range(6 - i):
            if lotto_num[j][k] + i == lotto_num[j][k + i]:
                lotto_in_a_row[i] += 1
                break

data = pd.DataFrame([[1092 - sum(lotto_in_a_row)]+lotto_in_a_row[1:6]], columns=['else','2_num', '3_num', '4_num', '5_num', '6_num'])
data.to_csv('lotto_in_a_row.csv', index=False)