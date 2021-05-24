motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles[0] = 'honda'

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0, 'ducati')
del motorcycles[0]
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles.insert(1, '?')
errorValue = motorcycles.pop(1)
print(errorValue)
print(motorcycles)

'''
总结:
    ListName.pop(index) 和 del ListName[index] 都能够删除目标元素
    当需要用到这个被删除的元素时,使用pop;
    当不需要用到该元素时,使用del
'''

motorcycles.append('ducati')
motorcycles.remove('ducati')
print(motorcycles)

motorcycles.append('ducati')
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(f"\nA {too_expensive.title()} is too expensive for me.")