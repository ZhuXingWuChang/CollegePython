like_nums = {
    'Alice': [1, 2, 3],
    'Bob': [2, ],
    'Cindy': [3, 6, 9, ],
    'David': [4, 8, ],
    'Eric': [5, 8, ],
}

for name, numbers in like_nums.items():
    print(f"{name} likes number is: ")
    for number in numbers:
        print(f"\t{number}")
