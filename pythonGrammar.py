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
