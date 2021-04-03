'''
    需求：爬取糗事百科中任意页数的图片
    https://www.qiushibaike.com/imgrank/

    我们又发现第二页的url是
    https://www.qiushibaike.com/imgrank/page/2/
    所以可以找到url的规律
'''
import requests
import re
import os

if __name__ == '__main__':
    # UA伪装
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x6"
                      "4) AppleWebKit/537.36 (KHTML, like Gecko"
                      ") Chrome/89.0.4389.90 Safari/537.36 Edg/8"
                      "9.0.774.63"
    }
    # 对应的url
    for i in range(1, 4):
        page_url = 'https://www.qiushibaike.com/imgrank/page/' + str(i) + '/'
        # 从url中获取对应的数据,这里是text/html数据
        page_text = requests.get(url=page_url, headers=headers).text
        # 下面使用正则表达式, 从对应的html数据中解析出需要的图片
        r_ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        # re.findall()方法, 参数1是正则表达式, 参数2是解析的内容, 参数3在用于数据解析的时候必须是re.S
        # 这个方法会返回一个列表, 列表中包含了正则表达式提取出来的数据
        image_src_list = re.findall(r_ex, page_text, re.S)
        # print(image_data_list)

        if not os.path.exists('./糗图图片'):  # 如果在当前路径下不存在"糗图图片"文件夹
            os.mkdir('./糗图图片')  # 那么在当前路径下创建一个名为"糗图图片"的文件夹

        for src in image_src_list:
            # image_src就是每张图片的url
            image_src = 'https:' + src
            # 获得图片的二进制数据
            image_data = requests.get(url=image_src, headers=headers).content
            # 给图片命名, 按照'/'把字符串切开, 最后一个就是图片原来的名字
            image_name = src.split('/')[-1]
            # 将图片存到文件夹中
            with open('./糗图图片/' + image_name, 'wb') as fp:
                fp.write(image_data)
            print(image_name, '爬取完毕!')
