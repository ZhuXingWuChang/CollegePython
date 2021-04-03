import requests

if __name__ == '__main__':
    # 获取url
    url = "https://pic.qiushibaike.com/system/picture" \
          "s/12420/124202170/medium/BGZ5SG7QY9WVMJL9.jpg"
    # UA伪装
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x6"
                      "4) AppleWebKit/537.36 (KHTML, like Gecko"
                      ") Chrome/89.0.4389.90 Safari/537.36 Edg/8"
                      "9.0.774.63"
    }
    # content:内容    因为图片是用二进制矩阵存储的，所以不能对得到的请求使用.text
    # 而是要使用.content 来返回二进制形式的数据
    # .text返回对应的字符串数据, .json()返回json数据, .content返回二进制数据
    image_data = requests.get(url=url, headers=headers).content

    with open('./糗图.jpg', 'wb') as fp:
        fp.write(image_data)
