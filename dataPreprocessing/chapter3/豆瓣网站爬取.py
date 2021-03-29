import requests

if __name__ == '__main__':
    url = 'https://movie.douban.com/j/search_subjects'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63 '

    }
    params = {
        'type': 'movie',
        'tag': '日本',
        'sort': 'recommend',
        'page_limit': '1000',
        'page_start': '0',
    }
    response_json = requests.get(url=url, params=params, headers=headers).json()
    messageList = []
    for movie in response_json['subjects']:
        messageList.append(f"电影名称:{movie['title']},电影评分:{movie['rate']}")
    with open('./豆瓣电影评分.txt', 'w', encoding='utf-8') as fp:
        fp.write(str(messageList))
