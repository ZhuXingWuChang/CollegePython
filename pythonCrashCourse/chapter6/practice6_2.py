like_nums = {
    'Alice': 1,
    'Bob': 2,
    'Cindy': 3,
    'David': 4,
    'Eric': 5,
}

for name in like_nums.keys():
    print(f"{name} likes number is {like_nums.get(name)}.")
