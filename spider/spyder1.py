import requests
# step1 : 指定url
url = 'https://search.bilibili.com/all'
keyWord = input('Enter a key word:')
params = {'spm_id_from': keyWord}
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
