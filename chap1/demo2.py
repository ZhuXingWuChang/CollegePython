# 转义字符
print('hello\nworld')  # 换行
print('hello\tworld')  # 制表符
print('helloooo\tworld')  # 制表符
print('hello\rworld')  # 回车
print('hello\bworld')  # 退格

print('http:\\\\www.baidu.com')  # 反斜杠
print('老师说:\'大家好\'')  # 单引号
print('老师说:\"大家好\"')  # 双引号

# 原字符，不希望字符串中转义字符起作用，就使用元字符，就是在字符串前面加上r或R
print(r'hello\nworld')
# 注意事项，最后一个字符不能是单个反斜杠
# print(r'helloworld\') 会报错
print(r'helloworld\\')
