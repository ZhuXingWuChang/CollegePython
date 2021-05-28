cities = {
    '西安': {
        '国家': '中国',
        '人口': 500_000,
        '说明': '曾是封建中国时期的首都',
    },

    '南京': {
        '国家': '中国',
        '人口': 1000_000,
        '说明': '曾是中华民国时期的首都',
    },

    '北京': {
        '国家': '中国',
        '人口': 3000_000,
        '说明': '是现在中华人民共和国的首都',
    }

}

for city, city_info in cities.items():
    print(f"{city}:")
    for key, value in city_info.items():
        print(f"\t{key}: {value}")
