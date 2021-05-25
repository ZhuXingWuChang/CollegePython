my_pizzas = ['A', 'B', 'C']
friend_pizzas = my_pizzas[:]

my_pizzas.append('DDD')
friend_pizzas.append('EEE')

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
