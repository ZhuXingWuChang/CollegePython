guest_list = ['张三', '李四', '老八', '赵六']
guest_list.insert(0, '王二麻子')
guest_list.insert(2, '老王')
guest_list.append('宇哥')

print("餐桌无法送达,很遗憾,只能邀请两位嘉宾了.")
delete_guest = guest_list.pop()
print(f"{delete_guest}先生,很抱歉,因为一些意外不能邀请您了!")
delete_guest = guest_list.pop()
print(f"{delete_guest}先生,很抱歉,因为一些意外不能邀请您了!")
delete_guest = guest_list.pop()
print(f"{delete_guest}先生,很抱歉,因为一些意外不能邀请您了!")
delete_guest = guest_list.pop()
print(f"{delete_guest}先生,很抱歉,因为一些意外不能邀请您了!")
delete_guest = guest_list.pop()
print(f"{delete_guest}先生,很抱歉,因为一些意外不能邀请您了!")

print(f"{guest_list[0]}先生,请您继续与我共进晚餐!")
print(f"{guest_list[1]}先生,请您继续与我共进晚餐!")

del guest_list[0]
del guest_list[0]

print(guest_list)
