user_names = ['admin', 'alice', 'bob', 'cindy', 'david']

for user_name in user_names:
    if user_name == 'admin':
        print(f"Hello {user_name}, would you like to see a status report?")
    else:
        print(f"Hello {user_name}, thank you for logging in again.")
