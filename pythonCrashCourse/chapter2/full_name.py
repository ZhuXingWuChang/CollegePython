first_name = "ada"
last_name = "lovelace"

# 这种字符串名为f字符串,f是format的简写,python通过把花括号内的变量替换为其值来设置字符串
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}!"
print(message)

# 对于Python 3.5之前的版本,没有这种"f语法",要使用如下方式
full_name = "{} {}".format(first_name, last_name)
