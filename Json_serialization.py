import json
friends1 = {'Bharat': [26, 'Mumbai', 410206], 'Pragati': [24, 'Mumbai', 400612], 'Shailesh': [26, 'Mumbai', 400043]}
friends2 = {'Durgesh': [24, 'Mumbai', 410216], 'Amit': [34, 'Mumbai', 400013], 'Rahul': [32, 'Mumbai', 400001]}
friends = (friends1, friends2)

with open('friends.json', 'w',) as f:
    json.dump(friends, f, indent= 4)

json_string = json.dumps(friends, indent= 4)
print(json_string)