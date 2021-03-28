"""
爬取药监总局中的企业详情数据
url: http://scxk.nmpa.gov.cn:81/xk/
需求:
    - 将首页中每一家企业的详情数据进行爬取(详情页对应的数据)
    - 将前2页的数据爬取即可
难点:
    - 用不到数据解析
    - 所有的数据都是动态加载出来的
提示:
    - 先试着将一家企业的详情页的详情数据爬取出来,然后再取爬取多家企业的数据
"""
import requests

if __name__ == '__main__':
    url = 'http://scxk.nmpa.gov.cn:81/xk/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; '
                      'x64) AppleWebKit/537.36 (KHTML, like '
                      'Gecko) Chrome/89.0.4389.90 Safari/537'
                      '.36 Edg/89.0.774.63'
    }
    page_text = requests.get(url=url, headers=headers).text
    with open('./化妆品.html', 'w', encoding='utf=8') as fp:
        fp.write(page_text)
