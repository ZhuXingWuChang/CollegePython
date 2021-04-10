"""
需求:爬取58二手房中的房源信息
https://bj.58.com/ershoufang/

步骤:
1. 爬取到页面源码数据
2. 进行数据解析
    1. 实例化一个etree对象
    2. 用xpath表达式进行定位,获取li标签的列表对象
    3. 遍历列表,解析出存储标题的a标签
    4. 进行持久化存储
"""
import requests
from lxml import etree

if __name__ == '__main__':
    url = 'https://bj.58.com/ershoufang/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                      ' (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/'
                      '89.0.774.75'
    }
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    div_list = tree.xpath('//div[@class="list"]//section[@class="list"]//div')
    fp = open('./二手房信息.txt', 'w', encoding='utf-8')
    for i in range(0, 13 * 30, 13):
        div = div_list[i]
        title = div.xpath('.//div[@class="property-content-title"]/h3/text()')
        if len(title) != 0:
            strTitle = title[0]
        print(strTitle)
        fp.write(strTitle + '\n')
