# 给sort()方法传入reverse=True参数,会使列表本身被修改(可变对象)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

cars.sort()
print(cars)

# 使用sorted(ListName)方法,会返回一个新的排序后的列表(不可变对象)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))

print("\nHere is the original list agian: ")
print(cars)

# ListName.reverse()会修改列表,使其倒序
print()
print(cars)
cars.reverse()
print(cars)

print(len(cars))
