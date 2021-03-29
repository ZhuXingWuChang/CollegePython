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
import json

if __name__ == '__main__':
    page_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'
    }
    for page_num in range(2):
        page_params = {
            'on': 'true',
            'page': str(page_num),
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
        }
        page_response_json = requests.post(url=page_url, params=page_params, headers=headers).json()
        for i in page_response_json['list']:
            item_id = i['ID']
            item_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
            item_params = {
                'id': item_id
            }
            item_response_json = requests.post(url=item_url, params=item_params, headers=headers).json()
            print("*企业负责人:", item_response_json['businessPerson'], " *企业名称:", item_response_json['epsName'],
                  " *许可项目:", item_response_json['certStr'])
