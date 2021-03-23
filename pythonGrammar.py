<<<<<<< HEAD
# ---------------------------python的注释---------------------------
# 单行注释

"""
    第一种多行注释
    第一种多行注释
"""

'''
    第二种多行注释
    第二种多行注释
'''

# ---------------------------python的变量---------------------------
# my_name = "张三"
# print(my_name)
#
# myAge = 23
# print(myAge)
#
# a = 1
# print(type(a))  # 整形
#
# b = 1.1
# print(type(b))  # 浮点型
#
# c = True
# print(type(c))  # 布尔型
#
# d = "12345"
# print(type(d))  # 字符串
#
# e = [10, 20, 30]
# print(type(e))  # 列表
#
# f = (10, 20, 30)
# print(type(f))  # 元组
#
# h = {10, 20, 30}
# print(type(h))  # 集合
#
# g = {"name": "张三", "age": 20}
# print(type(g))  # 字典

# ---------------------------print输出---------------------------
# print('hello Python')
#
# age = 18
# print(age)

# ---------------------------格式化字符串---------------------------
# name = "诸行无常"
# age = 18
# weight = 75.5
# student_id = 1
# print('我的名字是%s' % name)
# print('我的学号是%04d' % student_id)
# print('我的体重是%.2f公斤' % weight)
# print('我的名字是%s，今年%d岁了' % (name, age))
# print('我的名字是%s，明年%d岁了' % (name, age + 1))
# print('我的名字是{0}，明年{1}岁了'.format(name, age + 1))
# print('我的名字是{0}，今年{1}岁了'.format("诸行无常", 18))
# print(f'我的名字是{name}，明年{age + 1}岁了')
#
# print('我的名字是%s，今年%s岁了，我的体重是%s公斤' % (name, age, weight))  # 字符串拼接操作
#
# print('输出的内容', end='\n')  # 这会在末尾换行输出
# # 在Python中，print()默认自带 end='\n' 这个结束换行符
# print('内容', end=" ")  # 改变Python的默认换行符为 " "
# print('内容', end="...")  # 改变Python的默认换行符为 '...'
# print('\n')  # 这会输出两个换行符，因为结尾默认还有一个 end='\n'

# ---------------------------python的输入---------------------------
# 输入的用法 input("提示信息"）
# password = input('请输入您的密码：')
# print(f'您输入的密码是{password}')
# print(type(password))

# ---------------------------转换数据类型---------------------------
# a = 3.1
# print(int(a))
# b = 3
# print(float(b))

# ---------------------------体验转换数据类型---------------------------
# 需求：input接受用户输入，用户输入”1“，将这个数据1转换成整型
# num = input('请输入您的幸运数字：')
# print(f"您的幸运数字是{num}")
# print(type(num))  # 用户输入的类型都是str
# print(type(int(num)))  # str转换为int类型
#
# num1 = 1
# print(float(num1))
# print(type(float(num1)))
#
# num2 = 10
# print(type(str(num2)))

# list1 = [10, 20, 30]
# print(type(list1))
# print(tuple(list1))  # 将一个列表转换成元组
# print(type(tuple(list1)))

# t1 = (100, 200, 300)
# print(type(t1))
# print(list(t1))  # 将一个元组转换成列表
# print(type(list(t1)))

# str1 = '10'
# str2 = '[1, 2, 3]'
# str3 = '(1000, 2000, 3000)'
# str4 = '{123]'
# print(type(eval(str1)))  # eval()讲字符串中的数据换转成Python表达式的原本类型
# print(type(eval(str2)))
# print(type(eval(str3)))
# print(type(eval(str4)))  # 如果语法不对，那么会抛出异常

# ---------------------------运算符---------------------------
=======
# --------------------运算符--------------------
# print(8 / 3)  # 除法，会返回一个浮点数
# print(8 // 3)  # 整除，会返回一个整型数
# print(8.0 // 3.0)  # 整除，会返回一个浮点数
# print(9 % 4)  # 取余
# print(2 ** 10)  # 指数
#
# num1, float1, str1 = 10, 0.5, 'hello world'  # 多个变量赋值
# a = b = 10  # 相同变量赋值
# print(num1, a, b)  # 直接输出多个值
# print(float1)
# print(str1)

# b = 2
# b *= 3  # b = 2 * 3
#
# c = 10
# c += 1 + 2  # c = 10 + (1 + 2)
# print("b = %d, c = %d" % (b, c))
#
# c **= b  # c = 13 ^ 6
# print('%d = 13 ^ 6' % c)

# --------------------比较运算符--------------------
"""
python的比较运算符和C语言的一致
python有逻辑运算符and or not，这些运算符可以进行比较操作
还可以对数进行逻辑运算
"""
# a = 0
# b = 1
# c = 2
# print(a and b)  # 逻辑运算
# print(a or c)  # 逻辑运算
# print(b and c)  # 逻辑运算
# print(not a)  # 布尔运算
# print(not b)  # 布尔运算
# print(not c)  # 布尔运算

# --------------------条件运算符--------------------
# age = int(input('请输入您的年龄：'))  # 这里还要将str转换为int
# if age >= 18:
#     print(f'您的年龄是{age}，已经成年，可以上网')
# else:
#     print(f'您的年龄是{age}，未成年，不能上网')
# print('系统关闭')

# age = int(input('请输入您的年龄：'))
# if age < 18:
#     print(f'您的年龄是{age}，童工一枚')
# elif (age >= 18) and (age <= 60):  # 可以的条件可以使用 18 <= age <= 60
#     print(f'您的年龄是{age}，合法工龄')
# elif age > 60:
#     print(f'您的年龄是{age}，可以退休')

# money = 1  # 假设用money=1表示有钱，money=0表示没钱
# seat = 0
# if money == 1:
#     print('有钱，上车')
#     if seat == 1:
#         print('有空座')
#     else:
#         print('没有空座')
# else:
#     print('没钱，下车')
>>>>>>> origin/main
