import numpy as np

# 创建一维数组
arr1 = np.array([1, 2, 3])
print(arr1)

# 创建多维数组
arr2 = np.array([[1, 2], [3, 4], [5, 6]])
print(arr2)

# 数组基本运算
print("数组的维数：", arr2.ndim)
print("数组元素总个数：", arr2.size)
print("元素类型：", arr2.dtype)

# 创建常数数组
arr3 = np.zeros((2, 3), dtype=float, order='C')
print("创建0数组：", arr3)

arr4 = np.ones([2, 3], dtype=None, order='C')
print("创建1数组：", arr4)

# 使用数值范围创建数组
arr5 = np.arange(1, 10, 2, dtype=float)
print(arr5)

# 切片和索引
arr6 = np.arange(20)  # 创建一个从0到19，长度为20的数组
s = slice(1, 20, 3)  # 从索引1开始到索引20为止，步长为3
print(arr6[s])

b = arr6[2:14:2]  # 从索引2到索引14停止，补偿为2
print(b)
