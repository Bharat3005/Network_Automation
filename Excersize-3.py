import json
def serialize():
    my_mates = {'Bharat': [26, 'Mumbai', 410206], 'Pragati': [24, 'Mumbai', 400612], 'Shailesh': [26, 'Mumbai', 400043]}
    with open('my_mates.dat', 'wb') as f:
        json.dump(my_mates, f)

    serialize()
