"""
分页数据的爬取操作
    爬取肯德基的餐厅位置数据
        url: https://www.kfc.com.cn/kfccda/storelist/index.aspx
分析
    1.在录入关键字文本框中,输入关键字,按下搜索按钮,url并没有变,说明发起的是一个ajax请求
        - 当前页面刷新出来的位置信息一定是通过ajax请求得到的数据
        什么是ajax: https://wiki.jikexueyuan.com/project/ajax/what-is.html
    2.基于抓包工具定位到该ajax请求的数据包,从该数据包中捕获到:
        (1)请求的url
        (2)请求方式
        (3)请求携带的参数
        (4)响应数据
"""
import requests

url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/5'
                  '37.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537'
                  '.36 Edg/89.0.774.63'
}

keyWord = input('输入查询的地点:')
num = input('输入要查询的页数:')
for page in range(1, int(num) + 1):
    data = {
        'cname': '',
        'pid': '',
        'keyword': keyWord,
        'pageIndex': str(page),
        'pageSize': '10'
    }
    # data参数是post方法中处理参数动态化的参数
    response = requests.post(url=url, data=data, headers=headers)
    page_text = response.json()

    for i in page_text['Table1']:
        title = i['storeName']
        address = i['addressDetail']
        print(title, address)
