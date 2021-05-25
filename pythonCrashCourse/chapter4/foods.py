my_foods = ['pizza', 'falafel', 'carrot cake']
# 如果这里省略掉最后的[:],那么这两个变量会指向同一块内存
friend_foods = my_foods[:]

my_foods.append('connoli')
friend_foods.append('ice cream')

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)
