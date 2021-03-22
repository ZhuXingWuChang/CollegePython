a = 3.14159
print(a, type(a))
n1 = 1.1
n2 = 2.2
print(n1 + n2)  # 二进制数无法精确表示所有十进制数，存在误差

from decimal import Decimal

print(Decimal('1.1') + Decimal('2.2'))  # 可以Decimal函数解决精度问题
