#  로또 번호 크롤링 후 csv 파일로 얻기
#  lxml pip 필수
#  참조 https://teddylee777.github.io/python/lotto/
import requests
import pandas as pd
from bs4 import BeautifulSoup


# 최신 회차 크롤링 함수
def get_max_count():
    url = 'https://dhlottery.co.kr/common.do?method=main'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    max_count = int(soup.find('strong', id='lottoDrwNo').text)
    return max_count


# 크롤링 함수
def crawling_lotto(count):
    # url에 회차를 실어 페이지 조회
    url = f'https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={count}'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')

    win_number = [int(i) for i in soup.find('div', class_='num win').find('p').text.strip().split('\n')]
    bonus_number = int(soup.find('div', class_='num bonus').find('p').text.strip())

    return win_number, bonus_number


max_count = get_max_count()
lotto = pd.DataFrame(index=range(1, max_count + 1), columns=['num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'bonus'])
for i in range(1, max_count + 1):
    print("progress is %0.2f%%" % ((i/max_count) * 100))
    six_number, bonus_number = crawling_lotto(i)
    lotto.loc[i, 'num1'], lotto.loc[i, 'num2'], lotto.loc[i, 'num3'] = six_number[0], six_number[1], six_number[2]
    lotto.loc[i, 'num4'], lotto.loc[i, 'num5'], lotto.loc[i, 'num6'] = six_number[3], six_number[4], six_number[5]
    lotto.loc[i, 'bonus'] = bonus_number
print("Done")
lotto.to_csv('lotto.csv', index=True)