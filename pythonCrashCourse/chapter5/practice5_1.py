car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

new_car = car
print("\nThe 'new_car' equals 'car'?")
print(new_car == car)

new_car = 'subaru'
print("\nNow, the 'new_car' equals 'car'?")
print(new_car == car)

# Python中的'=='对字符串的判断进行过包装,只要字符串内容一致,就会返回True
