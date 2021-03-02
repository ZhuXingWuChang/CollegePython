# 可以输出数字
print(520)
print(98.5)

# 可以输出字符串
print('Hello World')
print("Hello World")

# 含有运算符的表达式
print(3 + 1)

# 输出到文件中
fp = open('/text.txt', 'a+')
print('helloworld', file=fp)
fp.close()

# 不进行换行输出
print('hello', 'world', 'Python')
