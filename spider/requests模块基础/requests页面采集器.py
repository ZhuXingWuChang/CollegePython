import requests
# step1 : 指定url
url = 'https://www.google.com/search?'
keyWord = input('Enter a key word:')
params = {'q': keyWord}
# 面对UA检测, 我们使用UA伪装, 让爬虫使用浏览器的身份标识
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                  ' (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'}
# step2: 发起请求, get方法会返回一个响应对象
response = requests.get(url=url, params=params, headers=headers)
response.encoding = 'utf-8'
# step3: 获取响应数据
page_text = response.text

# step4: 持久化存储
fileName = keyWord + '.html'
with open(fileName, 'w', encoding='utf-8') as fp:
    fp.write(page_text)
print(keyWord, '抓取完毕！')
