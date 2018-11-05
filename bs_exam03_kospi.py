# 금융 공학 레시피
import bs4
import datetime as dt
from bs4 import BeautifulSoup
from urllib.request import urlopen

#/html/body/div/table[1]/tbody/tr[3]/td[1]
index_code = "KPI200" # 주소 변수화
page_number = 1
naver_index = 'https://finance.naver.com/sise/sise_index_day.nhn?code='+ \
                index_code + '&page=' + str(page_number)

source = urlopen(naver_index).read()
source = bs4.BeautifulSoup(source, "lxml")

#print(source.prettify) # 전체 소스 보여줘
#print(soup.title.text)

td = source.find_all("td")
#print(len(td))

# XPath를 통해 확인된 값(날짜-검사-Copy XPath) - 프론트엔드 개발자
#/html/body/div/table[1]/tbody/tr[3]/td[1]
#print(source.find_all("table")[0].find_all("tr")[2].find_all("td")[0].text)
#print(source.find_all("table")[0].find_all("tr")[2].find_all("td")[1].text)
# date 클래스 객체화
d = source.find_all("td", class_ = "date")[0].text
print(d)

yyyy = int(d.split('.')[0])
mm = int(d.split('.')[1])
dd = int(d.split('.')[2])
this_date = dt.date(yyyy, mm, dd)
print(this_date)

# 날짜 구하는 함수 만들기
def date_format(d) :
    d = str(d).replace('-', '.')
    yyyy = int(d.split('.')[0])
    mm = int(d.split('.')[1])
    dd = int(d.split('.')[2])
    this_date = dt.date(yyyy, mm, dd)
    return this_date

print(date_format(this_date))
# 종가 1
this_close = source.find_all("tr")[2].find_all("td")[1].text
this_close = this_close.replace(',', '')
this_close = float(this_close)
print(this_close) # 종가(문자열이 아닌 실수값)
# 종가 2
p = source.find_all("td", class_ = "number_1")[0].text
print(p)

dates = source.find_all("td", class_ = "date")
price = source.find_all("td", class_ = "number_1")
print(len(dates))
print(len(price))

for n in range(len(dates)) :
    this_date = dates[n].text
    this_date = date_format(this_date) # 날짜 추출

    this_close = price[n*4].text
    this_close = this_close.replace(',', '')
    this_close = float(this_close)
    print(this_date)
    print(this_close)

# page_number
paging = source.find("td", class_ = "pgRR").find('a')["href"]
print(paging)
paging = paging.split('&')[1] # & 기준으로 자름 0, 1
print(paging)
paging = paging.split('=')[1]
print(paging)
