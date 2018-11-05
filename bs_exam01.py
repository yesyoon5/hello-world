from bs4 import BeautifulSoup
# import BeautifulSoup as bs4

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, "html.parser")
#print(soup.prettify())
#print(soup.title)
#print(soup.title.text)
#print(soup.title.string)

# 하이퍼링크 가져오기(주소 하나 / 다 가져오기)
#print(soup.a)
#print(soup.find_all('a'))

#print(soup.find_all('a')[2].text) << 오류 발생함. 아래처럼 객체로 만들어야
#print(soup.find_all('a')[2])

#모든 값은 순환하며 출력(객체) a 태그 - 하이퍼링크 만들 때 씀
link = soup.find_all('a')
for i in link :
    print(i.text)
