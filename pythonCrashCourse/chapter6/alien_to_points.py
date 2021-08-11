alien_0 = {'color': 'green', 'speed': 'slow'}

# 方法get()的第一个参数用于指定键,是必不可少的
# 第二个参数为指定的键不存在时要返回的值
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# 如果指定的键有可能不存在,应考虑使用方法get(),而不要使用方括号表示法
