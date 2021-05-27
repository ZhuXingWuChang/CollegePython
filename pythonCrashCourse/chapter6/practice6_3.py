explains = {
    '变量': '在内存中开辟一段指定的空间,用来存放值',
    '指针': '这段空间有地址,指针保存空间的地址',
    '列表': '可修改,用于存放一系列的值',
    '字典': '存放键值对',
}

for key in explains.keys():
    print(key + ":")
    print("\t" + explains[key])
