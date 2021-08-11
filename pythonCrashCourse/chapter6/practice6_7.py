users = {
    '张三': {
        'first_name': '三',
        'last_name': '张',
        'age': 40,
        'city': '广东',
    },

    '李四': {
        'first_name': '四',
        'last_name': '李',
        'age': 35,
        'city': '广西',
    },
}

for user, user_info in users.items():
    print('-----------')
    print("名字: " + user)
    print(f"年龄: {user_info['age']}")
    print("城市: " + user_info['city'])
