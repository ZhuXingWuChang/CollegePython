import requests

url = 'https://search.bilibili.com/all'
keyWord = input('Enter a key word:')
params = {'spm_id_from': keyWord}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                  ' (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63'}
resopnse = requests.get(url=url, params=params, headers=headers)
resopnse.encoding = 'utf-8'
page_text = resopnse.text
fileName = keyWord + '.html'
with open(fileName, 'w', encoding='utf-8') as fp:
    fp.write(page_text)
print(keyWord, '抓取完毕！')
