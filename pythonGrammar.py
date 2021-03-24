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
'''
实例：网吧上网
'''
# age = int(input('请输入您的年龄：'))  # 这里还要将str转换为int
# if age >= 18:
#     print(f'您的年龄是{age}，已经成年，可以上网')
# else:
#     print(f'您的年龄是{age}，未成年，不能上网')
# print('系统关闭')
'''
实例：工龄判断
'''
# age = int(input('请输入您的年龄：'))
# if age < 18:
#     print(f'您的年龄是{age}，童工一枚')
# elif (age >= 18) and (age <= 60):  # 可以的条件可以使用 18 <= age <= 60
#     print(f'您的年龄是{age}，合法工龄')
# elif age > 60:
#     print(f'您的年龄是{age}，可以退休')
'''
实例：坐公交
'''
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
'''
初始版：猜拳游戏
提示：0-石头，1-剪刀，2-布
3.出拳：玩家输入出拳；电脑随机出拳
4.判断输赢：玩家获胜；平局；电脑获胜
'''
# import random  # 导入random模块
#
# computer = random.randint(0, 2)  # 电脑在0和2之间随机选择数字（包括0和2）
# print(computer)
# player = int(input("请出拳：0-石头，1-剪刀，2-布："))
# if (player == 0 and computer == 1) or (player == 1 and computer == 2) or (player == 2 and computer == 0):
#     print('玩家获胜')
# elif player == computer:
#     print('平局')
# else:
#     print('电脑获胜')

'''
进阶版：猜拳游戏
'''
# import random
# import sys
#
# print("-----欢迎来到人机对战小游戏-----")
# name = input('请输入您的游戏名：')
# while True:
#     stats = input('欢迎"%s"来到本游戏，输入Y开始游戏，输入N推出游戏，请您输入：' % name)
#     if stats == 'Y' or stats == 'y':
#         print('游戏开始......')
#         print('0-石头，1-剪刀，2-布')
#         break
#     elif stats == 'N' or stats == 'n':
#         print('游戏结束......')
#         sys.exit(0)
#     else:
#         print('请按照要求重新输入！')
# print('------------加载中------------')
#
#
# def Game(user, comp):
#     if (user == 0 and comp == 1) or (user == 1 and comp == 2) or (user == 2 and comp == 0):
#         print("机器输入%d，您赢了！" % comp)
#     elif user == comp:
#         print("机器输入%d，平局了！" % comp)
#     else:
#         print("机器输入%d，您输了！" % comp)
#     res = input("重新游戏请输入x，退出游戏按任意键")
#     if res == 'x' or res == 'X':
#         return
#     else:
#         sys.exit(0)
#
#
# while True:
#     user = int(input('请您出拳，输入相应数字！'))
#     if user == 0 or user == 1 or user == 2:
#         comp = random.randint(0, 2)
#         Game(user, comp)
#     else:
#         print('输入数字有误，请确认后，重新输入！')

# ------------三目运算符------------
# a = 1
# b = 2
#
# c = a if a > b else b
# print(c)

# ------------while循环------------
'''
应用一：计算1~100累加和
'''
# i = 1
# result = 0
# while i <= 100:
#     result += i
#     i += 1
# print(result)
'''
应用二：计算1~100偶数累加和
'''
# # 方法一：条件判断，如果模2为0，则是偶数，累加
# i = 1
# result = 0
# while i <= 100:
#     if i % 2 == 0:
#         result += i
#     i += 1
# print(result)
# # 方法二：计数器控制增量为2
# i = 0
# result = 0
# while i <= 100:
#     result += i
#     i += 2
# print(result)

# ------------break和continue------------
'''
break实例
'''
# i = 1
# while i <= 5:
#     if i == 4:
#         print(f'吃饱了不吃了')
#         break
#     print(f'吃了第{i}个苹果')
#     i += 1
'''
continue实例
'''
# i = 1
# while i <= 5:
#     if i == 3:
#         print(f'大虫子，第{i}个不吃了')
#         i += 1
#         continue
#     print(f'吃了第{i}个苹果')
#     i += 1

# ------------while循环嵌套------------
'''
应用一：打印星号（正方形）
'''
# j = 0
# while j <= 4:
#     i = 0
#     while i <= 4:
#         print('*', end='')
#         i += 1
#     print()
#     j += 1
'''
应用二：打印星号（三角形）
'''
# j = 0
# while j <= 4:
#     i = 0
#     while i <= j:
#         print('*', end='')
#         i += 1
#     print()
#     j += 1
'''
应用三：打印星号（三角形）
'''
# j = 1
# while j <= 9:
#     i = 1
#     while i <= j:
#         print(f'{i}*{j}={i * j}', end='\t')
#         i += 1
#     print()
#     j += 1

# ------------for循环------------
'''
for循环语法如下
for 临时变量 in 序列:
    循环体
'''
# str1 = 'Hello World'
# for i in str1:
#     print(i)

# str1 = 'Hello World'
# for i in str1:
#     if i == 'e':
#         print('遇到e不打印')
#         break
#     print(i)

# str1 = 'Hello World'
# for i in str1:
#     if i == 'e':
#         print('遇到e不打印')
#         continue
#     print(i)

# ------------while...else------------
'''
while 条件:
    条件成立重复执行的代码
else:
    循环正常结束后要执行的代码
'''
# 示例
# i = 1
# while i <= 5:
#     print('Hello World')
#     i += 1
# else:
#     print('执行完毕')

# break终止循环
# i = 1
# while i <= 5:
#     if i == 3:
#         print('提前结束')
#         break
#     print('Hello World')
#     i += 1
# else:
#     print('执行完毕')

# continue控制循环
# i = 1
# while i <= 5:
#     if i == 3:
#         print('打断一下')
#         i += 1
#         continue
#     print('Hello World')
#     i += 1
# else:
#     print('执行完毕')

# ------------for...else------------
'''
for 临时变量 in 序列:
    重复执行的代码
    ...
else:
    循环正常结束之后要执行的代码
'''
# 示例
# str1 = 'Hello World'
# for i in str1:
#     print(i)
# else:
#     print('循环正常结束之后执行的代码')

# break终止循环
# str1 = 'Hello World'
# for i in str1:
#     if i == 'e':
#         print('遇到e不打印')
#         break
#     print(i)
# else:
#     print('循环正常结束之后执行的代码')

# continue控制循环
# str1 = 'Hello World'
# for i in str1:
#     if i == 'e':
#         print('遇到e不打印')
#         continue
#     print(i)
# else:
#     print('循环正常结束后执行的代码')

# ------------字符串------------
# a = 'Hello World'
# b = "abcdefg"
# print(type(a))
# print(type(b))

# name1 = 'Tom'  # 单引号字符串
# name2 = "Rose"  # 双引号字符串
# name3 = '''Tom'''  # 三单引号字符串
# name4 = """Rose"""  # 三双引号字符串
# a = ''' I am Tom,
#         nice to meet you! '''
# b = """ I am Rose,
#         nice to meet you! """
# print(a, '\n', b)

# c = "I'm Tom"
# d = 'I\'m Tom'

# print('hello world')
#
# name = 'Tom'
# print('My name\'s %s' % name)
# print(f"My name's {name}")

# 在Python中，用户用input输出的都是字符串
# name = input('Type in your name, please:')
# print(f'Your name\'s {name}')
# print(type(name))
# password = input('Type in your password, please:')
# print(f"Your password's {password}")
# print(type(password))

# 字符串的下标，即字符串的索引
# name = "abcdef"
# print(name[1])
# print(name[0])
# print(name[2])

# ------------字符串的切片操作------------
'''
序列[开始位置的下标:结束位置的下标:步长]
'''
# name = "abcdef"
# print(name[2:5:1])
# print(name[2:5])
# print(name[:5])
# print(name[1:])
# print(name[:])
# print(name[::2])
# print(name[:-1])  # -1表示倒数第一个数据, 所以这个地方输出到f前面停下
# print(name[-4:-1])
# print(name[::-1])

# ------------字符串的查找------------
'''
所谓查找就是查找子串在字符串中出现的位置，或出现的次数
find(): 检测某个子串是否在字符串中，如果在，返回下标，否则返回-1
语法:
字符串对象.find(子串, 开始位置的下标, 结束位置的下标)
'''
# myStr = "Hello world and string and list and Python"
# print(myStr.find('and'))  # 返回整个字符串内第一个and的首地址
# print(myStr.find('and', 15, 30))  # 返回15到30下标内第一个and的首地址
# print(myStr.find('ands'))  # 字符串里面没有这个，返回-1

'''
index(): 检测某个子串是否包含在这个字符串中，如果在，返回下标，否则报异常
语法:
字符串对象.index(子串, 开始位置的下标, 结束位置的下标)
'''
# myStr = "Hello world and string and list and Python"
# print(myStr.index('and'))
# print(myStr.index('and', 15, 30))
# print(myStr.index('aa'))

'''
rfind(): 和find()一样，但是查找方向是从右侧开始
rindex(): 和index()一样，但是查找方向是从右侧开始

count(): 返回某个子串在字符串中出现的次数
语法:
字符出对象.count(子串, 开始位置的下标, 结束位置的下标)
'''
# myStr = "Hello world and string and list and Python"
# print(myStr.count('and'))
# print(myStr.count('aa'))
# print(myStr.count('and', 0, 21))

# ------------字符串的修改------------
'''
所谓修改字符串，指的就是通过函数的形式修改字符串中的数据

replace(): 替换字符串
语法:
字符串对象.replace(旧子串, 新子串, 替换次数)
'''
# myStr = "Hello world and string and list and Python"
# print(myStr.replace('and', 'or'))
# print(myStr.replace('and', 'or', 10))
# print(myStr.replace('and', 'or', 1))  # 因为只替换1次，所以只有第一个and被or替换了
# print(myStr)  # 和Java一样，Python的str属于不可变对象

'''
split(): 按照指定字符分割字符串，如果分割字符是原有字符串中的子串，分割后会丢失该子串
语法
字符串序列.split(分割字符, num)
'''
# print(myStr.split('and'))
# print(myStr.split('and', 2))
# print(myStr.split(' '))
# print(myStr.split(' ', 2))
# print(myStr.split('中文'))

'''
join(): 用一个字符或子串合并成新的字符串
语法:
字符类型或字符串对象.join(多字符串组成的序列)
'''
# list1 = ['hello', 'python', 'list']
# t1 = ('aa', 'b', 'cc', 'ddd')
# print('_'.join(list1))
# print('...'.join(t1))

'''
capitalize(): 将字符串第一个字符转换成大写, 其余的小写
'''
# print('helLO'.capitalize())

'''
title(): 将字符串每个单词首字母转换成大写, 其余的小写
'''
# print('heLLo woRld aNd python'.title())

'''
lower(): 将字符串中大写转小写
'''
# print('HEllo WoRlD'.lower())

'''
upper(): 将字符串中小写转大写
'''
# print('HEllo WoRlD'.upper())

# ------------逻辑表达式 判断------------
'''
startswith(): 检查字符串是否以指定子串开头，是则返回True，否则返回False。
    如果设置开始和结束位置下标，则在指定范围内检查。
语法:
字符串对象.startswith(子串, 开始位置下标, 结束位置下标)
'''
# myStr = "Hello world and string and list and Python"
# print(myStr.startswith('Hello'))
# print(myStr.startswith('hello', 5, 20))

'''
endswith(): 检查字符串是否以指定子串结尾
语法:
字符串对象.endswith(子串， 开始位置下标, 结束位置下标)
'''
# myStr = "Hello world and string and list and Python"
# print(myStr.endswith('Python'))
# print(myStr.endswith("python"))
# print(myStr.endswith('Python', 2, 20))

'''
isalpha(): 如果字符串非空，且内容都是字母，返回True，否则返回False
'''
# myStr1 = 'hello'
# myStr2 = 'hello12345'
# print(myStr1.isalpha())
# print(myStr2.isalpha())

'''
isdigit(): 如果非空字符串中只包含数字，返回True，否则返回False
'''
# myStr1 = 'aaa12345'
# myStr2 = '12345'
# print(myStr1.isdigit())
# print(myStr2.isdigit())

'''
isalnum(): 如果字符串中至少有一个字符，并且所有字符都是字母 或 数字，返回True，否则返回False
'''
# myStr1 = 'aaa12345'
# myStr2 = '12.345'
# print(myStr1.isalnum())
# print(myStr2.isalnum())

'''
isspace(): 如果字符串中只包含空白，返回True，否则返回False
'''
# myStr1 = '1 2 3 4 5'
# myStr2 = '         '
# myStr3 = ''
# print(myStr1.isspace())
# print(myStr2.isspace())
# print(myStr3.isspace())  # 空串是没有空白的

# ------------列表------------
'''
[数据1, 数据2, 数据3, ......]
列标可以存储不同类型的数据，并且可以重复
对列表的后续操作可以有：增、删、减、改、查
'''
nameList = ['Tom', 'Lily', 'Rose', 'Lily', 1, 2]
# print(nameList[0])
# print(nameList[1])
# print(nameList[2])
# print(nameList.index('Lily', 0, 2))  # 从0开始，到2为止，不包含2
# # print(nameList.index('Alice'))  # 会报错
# print(nameList.count('Lily'))  # 统计出现次数
# print(len(nameList))

# print('Lily' in nameList)
# print('Alice' in nameList)
# print('Lily' not in nameList)
# print('Alice' not in nameList)

# nameList.append('xiaoming')
# print(nameList)  # 由此可见，列表是可变对象

# nameList.append(['xiaohu', '369'])
# print(nameList)  # 会将这个列表整体作为一个数据添加到列表

# nameList.extend('Karsa')  # 会把这些字符串拆开逐个添加到列表
# nameList.extend('123')
# print(nameList)

# nameList.insert(0, 'Jiejie')
# # del nameList  # 将整个内存都释放掉
# del nameList[0]  # 删除指定下标的数据
# print(nameList)

# del_name = nameList.pop(1)
# print(del_name)
# print(nameList.pop())  # 默认删除最后一个
# print(nameList)

# nameList.remove('Lily') # remove会找到第一个对应的Lily并删除
# print(nameList)

# print(nameList.clear())  # 清空数据但是不释放内存
# print(nameList)

# nameList.reverse()  # 倒置
# print(nameList)

# nameList.sort()  # 只能对可比较的数据排序，所以会报错
# numList = [1, 3, 5, 2, 4, 6, 9, 8, 7]
# numList.sort()
# print(numList)

# nameList2 = nameList.copy()
# print(nameList2)

# i=0
# while i<len(nameList):
#     print(nameList[i])
#     i+=1

# for i in nameList:
#     print(i)

# name_list = [['小明', '小红', '小绿'], ['Tom', 'Lily', 'Rose'], ['张三', '李四', '王五']]
# print(name_list[0])
# print(name_list[0][1])
