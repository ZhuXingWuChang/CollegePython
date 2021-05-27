current_users = ['Alice', 'Bob', 'Cindy', 'David', 'Eric']
new_users = ['Alice', 'Bob', 'Tom', 'Jack', 'Jeff']

current_users_copy = [copy.lower() for copy in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_copy:
        print(f'用户名"{new_user}"已被使用!')
    else:
        print(f'用户名"{new_user}"未被使用!')

# 注意第七行,这里 new_user.lower() 之后, new_user 的值并未改变
# 说明Python中的str对象是不可变的
