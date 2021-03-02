# coding:utf8

"""
DESC: Python数据预处理之第一个分词程序范例
Author: 伏草惟存
Prompt: code in Python3 env
"""

import jieba

str = "道路千万条，安全第一条；行车不规范，亲人两行泪。"
print("原句: \n" + str)

seg_list = jieba.cut(str)
print("分词: \n" + "/".join(seg_list))