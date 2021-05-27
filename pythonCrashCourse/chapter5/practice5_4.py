# 版本1
print('版本1')

alien_color = 'green'
if alien_color == 'green':
    print("加五分")
else:
    print("加十分")

print('-----------')
# 版本2
print('版本2')

alien_color = 'red'
if alien_color == 'green':
    print("加五分")
if alien_color != 'green':
    print("加十分")
