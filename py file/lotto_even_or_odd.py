import pandas as pd
import csv

#  연속 홀수 or 짝수 나오는 경우의 수
lotto_even_or_odd = [0, 0]

f = open("lotto ~ 1092.csv", 'r')
rdr = csv.reader(f)
lotto_num = []
for line in rdr:
    lotto_num.append(line[1:7])
f.close()
lotto_num.pop(0)

#  odd number
for i in range(len(lotto_num)):
    cnt = 0
    for j in range(6):
        if int(lotto_num[i][j]) % 2 == 1:
            cnt += 1
    if cnt == 6:
        lotto_even_or_odd[0] += 1

#  even number
for i in range(len(lotto_num)):
    cnt = 0
    for j in range(6):
        if int(lotto_num[i][j]) % 2 == 0:
            cnt += 1
    if cnt == 6:
        lotto_even_or_odd[1] += 1

data = pd.DataFrame([lotto_even_or_odd], columns=['odd', 'even'])
data.to_csv('lotto_even_or_odd.csv', index=False)
