# 这个程序是为了练习如何编写注释
x = 10
y = 20
# 先保存x的值,现在x的值已经被保存了,所以覆盖掉x也没事
t = x
# 把y的值写到x的位置
x = y
# 再把保存过的x的值写到y的位置
y = t
print(x, y)
