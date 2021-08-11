favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

staffs = ['jen', 'eric', 'sarah', 'roby', 'sari']

for staff in staffs:
    if staff in favorite_languages.keys():
        print(f"{staff.title()}, 非常感谢您参与我们的调查.")
    else:
        print(f"{staff.title()}, 您可以参与到我们的调查当中吗?")
