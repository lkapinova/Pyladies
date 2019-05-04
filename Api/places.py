import json

with open('places.json', encoding='utf-8-sig') as f:
    places = json.load(f)

for place in places:
    print('{name} ({country})'.format_map(place))