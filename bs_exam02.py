from bs4 import BeautifulSoup
from urllib.request import urlopen

#html_doc = "http://www.lemite.com/product/list.html?cate_no=325"
html_doc = "http://www.4irsw.com/ngb5/"

soup = urlopen(html_doc).read()
soup = BeautifulSoup(soup, "html.parser")
#soup = BeautifulSoup(soup, "lxml")

#print(soup)
print(soup.title.text)
