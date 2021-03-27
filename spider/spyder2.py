import requests

url = 'https://movie.douban.com/j/search_subjects'
params = {
    'type': 'movie',
    'tag': '日本',
    'sort': 'recommend',
    'page_limit': '20',
    'page_start': '0'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; '
                  'x64) AppleWebKit/537.36 (KHTML, like G'
                  'ecko) Chrome/89.0.4389.90 Safari/537.3'
                  '6 Edg/89.0.774.63'
}

response = requests.get(url=url, params=params, headers=headers)

# json()方法会返回对应的json字典
page_text = response.json()
for movie in page_text['subjects']:
    name = movie['title']
    score = movie['rate']
    print(name, score)
