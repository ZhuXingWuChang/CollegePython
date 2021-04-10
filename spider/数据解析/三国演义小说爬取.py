"""
需求: 爬取三国演义小说所有队标题和章节内容
https://www.shicimingju.com/book/sanguoyanyi.html

步骤:
1. 对首页的页面数据进行爬取
2. 在首页中解析出章节的标题和详情页的url
    1. 实例化BeautifulSoup对象,需要将页面源码数据加载到该对象中
    2. 解析章节标题和详情url
3. 对详情页发起请求,解析出章节内容
4. 将章节内容存储到本地
"""
import requests
from bs4 import BeautifulSoup
import os

if __name__ == '__main__':
    main_url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit'
                      '/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }
    main_response = requests.get(url=main_url, headers=headers)
    main_response.encoding = 'utf-8'
    main_page_text = main_response.text
    main_soup = BeautifulSoup(main_page_text, 'lxml')
    li_list = main_soup.select('#main .book-mulu > ul > li')
    for li in li_list:
        title = li.a.string
        sub_url = 'https://www.shicimingju.com/' + li.a['href']
        sub_response = requests.get(url=sub_url, headers=headers)
        sub_response.encoding = 'utf-8'
        sub_page_text = sub_response.text
        sub_soup = BeautifulSoup(sub_page_text, 'lxml')
        content = sub_soup.find('div', class_='chapter_content').text

        fileName = title + '.txt'
        if not os.path.exists('./三国演义'):
            os.mkdir('./三国演义')
        with open('./三国演义/' + fileName, 'w', encoding='utf-8') as fp:
            fp.write(content)
        print(title, "爬取完毕!")
