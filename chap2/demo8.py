name = '张三'
age = 20

print(type(name), type(age))
# print('我叫' + name + '今年,' + age + '岁')
# 上面的代码，将str与int类型连接会报错，解决方案如下
print('我叫' + name + '今年,' + str(age) + '岁')  # 将int类型转换为了str类型

print('----------str()将其他类型转换为str类型----------------')
a = 10
b = 198.8
c = False
print(type(a), type(b), type(c))
# 转型不是永久的
print(str(a), str(b), str(c), type(a), type(b), type(c))
print(type(str(a)), type(str(b)), type(str(c)))

print('----------int()将其他类型转换为int类型----------------')
s1 = '128'
f1 = 98.7
s2 = '76.77'
ff = True
s3 = 'hello'
print(type(s1), type(f1), type(s2), type(ff), type(s3))
print(int(s1), type(int(s1)))  # 将str转换成int，str必须是数字串
print(int(f1), type(int(f1)))  # float转换成int，会阶段
# print(int(s2), type(int(s2))) #带小数点，所以报错了，这不是纯数字串
print(int(ff), type(int(ff)))
# print(int(s3), type(int(s3))) #同样会报错
