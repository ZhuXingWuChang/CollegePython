country_rivers = {
    'nile': 'egypt',
    'yellow river': 'china',
    'yangtze': 'china',
    'ganges river': 'india',
    'mississippi': 'america',
}

for river in country_rivers.keys():
    print(f"The {river.title()} runs through {country_rivers[river].title()}.")
