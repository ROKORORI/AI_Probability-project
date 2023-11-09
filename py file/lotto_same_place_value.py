import pandas as pd
import csv

#  연속 같은 자리 수 나오는 사건 0번 ~ 6번
lotto_same_place_value = [[0, 0, 0, 0, 0] for _ in range(7)]

f = open("lotto ~ 1092.csv", 'r')
rdr = csv.reader(f)
lotto_num = []
for line in rdr:
    lotto_num.append(line[1:7])
f.close()
lotto_num.pop(0)

# i * 10 = [0, 10, 20, 30, 40], cnt = 같은 자리의 수 개수
for i in range(5):
    for j in range(len(lotto_num)):
        cnt = 0
        for k in range(6):
            if 0 <= int(lotto_num[j][k]) - (i * 10) <= 9:
                cnt += 1
        lotto_same_place_value[cnt][i] += 1

data = pd.DataFrame(lotto_same_place_value, index=range(7), columns=['0~9', '10~19', '20~29', '30~39', '40~45'])
data.to_csv('lotto_same_place_value.csv', index=True)
