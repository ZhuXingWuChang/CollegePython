import requests
import json

if __name__ == '__main__':
    # step1: 指定url
    post_url = 'https://fanyi.baidu.com/sug'
    # step2: 进行UA伪装
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; '
                      'x64) AppleWebKit/537.36 (KHTML, like '
                      'Gecko) Chrome/89.0.4389.90 Safari/537'
                      '.36 Edg/89.0.774.63'
    }
    # step3: post请求参数处理(同get一致)
    word = input('Enter a word:')
    data = {
        'kw': word
    }
    # step4: 请求发送
    response = requests.post(url=post_url, data=data, headers=headers)
    # step5: 获取响应数据, json方法返回的是一个obj
    # 观察浏览器抓包的response, 得知是一个字典对象
    # json方法不是任何时候都可以使用的, 只有确认响应数据是json类型的, 才可以使用
    # 响应数据类型从抓包工具的Content-Type中查看
    dic_obj = response.json()

    # step6: 持久化存储
    fileName = word + '.json'
    fp = open(fileName, 'w', encoding='utf-8')
    json.dump(obj=dic_obj, fp=fp, ensure_ascii=False)

    print('over!!!')
