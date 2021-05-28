favorite_places = {
    '阿伟': ['网吧', '超商', '公园'],
    '彬彬': ['网吧', '超商', '学校'],
    '阿杰': ['网吧', '家里'],
}

for name, places in favorite_places.items():
    print(f"{name}经常喜欢去", end='')
    for place in places:
        print(f"{place} ", end='')
    print()
