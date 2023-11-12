import pandas as pd
import csv

num_cnt = [0] + [0] * 45

f = open("lotto ~ 1092.csv", 'r')
rdr = csv.reader(f)
lotto_num = []
for line in rdr:
    lotto_num.append(line[1:7])
f.close()
lotto_num.pop(0)

for i in lotto_num:
    for j in range(6):
        num_cnt[int(i[j])] += 1
number_list = list(num_cnt[1:])
print(number_list)
data = pd.DataFrame(number_list, index=range(1, 46), columns=['cnt'])
for i in range(1, 46):
    data.loc[i, 'cnt'] = num_cnt[i]
data.to_csv('lotto_num_cnt.csv', index=True)
