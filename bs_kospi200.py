import matplotlib.pyplot as plt
import bs4
import datetime as dt
from urllib.request import urlopen
#%matplotlib inline
import pandas as pd

def date_format(d):
    d = str(d).replace('-', '.')
    yyyy = int(d.split(".")[0])
    mm = int(d.split('.')[1])
    dd = int(d.split('.')[2])

    this_date = dt.date(yyyy, mm, dd)
    return this_date

def historical_index_naver(index_code, start_date='', end_date='', page_number=1, last_page=0):

    if start_date:
        start_date = date_format(start_date)
    else:
        start_date = dt.date.today()

    if end_date:
        end_date = date_format(end_date)
    else:
        end_date = dt.date.today()

    naver_index = 'https://finance.naver.com/sise/sise_index_day.nhn?code='+ \
                    index_code + '&page=' + str(page_number)


    source = urlopen(naver_index).read()
    source = bs4.BeautifulSoup(source, 'lxml')

    dates = source.find_all('td', class_='date')
    prices = source.find_all('td', class_='number_1')

    for n in range(len(dates)):
        if dates[n].text.split('.')[0].isdigit():

            #날짜처리
            this_date = dates[n].text               #n번째 dates 값 추출
            this_date = date_format(this_date)      #날짜 형식으로 변환

            if this_date <= end_date and this_date >= start_date:
                this_close = prices[n*4].text
                # 0, 4, 8 ... 등 4의 배수에 해당하는 종가지수 추출
                this_close = this_close.replace(',', '')
                this_close = float(this_close)

                #딕셔너리에 저장
                historical_prices[this_date] = this_close

            elif this_date < start_date:
                return historical_prices

    if last_page == 0 :
        last_page = source.find('td', class_='pgRR').find('a')['href']
        #마지막페이지 주소 추출
        last_page = last_page.split('&')[1]
        last_page = last_page.split('=')[1]
        last_page = int(last_page)

    if page_number < last_page:
        page_number = page_number + 1
        historical_index_naver(index_code, start_date, end_date, page_number, last_page)

    return historical_prices

index_code = 'KPI200'
historical_prices = dict()
kospi200 = historical_index_naver(index_code, '2017-1-1', '2018-11-4')
tmp = {'KOSPI200': kospi200}
df = pd.DataFrame(tmp)
print(df)

plt.figure(figsize=(10,5))
plt.plot(df['KOSPI200'])
plt.legend(loc=0)
plt.grid(True, color='0.7', linestyle=':', linewidth=1) #그리드 설정
plt.show()
