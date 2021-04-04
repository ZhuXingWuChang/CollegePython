import requests
from bs4 import BeautifulSoup

url = 'https://www.sogou.com/'
response = requests.get(url=url)
page_text = response.text
# 方式1: 通过请求到的html文档来构造一个bs4.BeautifulSoup对象
soup1 = BeautifulSoup(page_text, 'lxml')
print(type(soup1))
print(soup1)
# 方式2: 通过本地的html文档来构造一个bs4.BeautifulSoup对象
with open('./test.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
fp = open('./test.html', 'r', encoding='utf-8')
soup2 = BeautifulSoup(page_text, 'lxml')
print(type(soup2))
print(soup2)
