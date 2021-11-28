# friends = {'Bharat': [26, 'Mumbai', 410206], 'Pragati': [24, 'Mumbai', 400612], 'Shailesh': [26, 'Mumbai', 400043]}
# with open('friends.txt', 'w') as f:
#     f.write(friends)
# =======================================================================================++++#
#############Use of pickel#########################################


import pickle
friends1 = {'Bharat': [26, 'Mumbai', 410206], 'Pragati': [24, 'Mumbai', 400612], 'Shailesh': [26, 'Mumbai', 400043]}
friends2 = {'Durgesh': [24, 'Mumbai', 410216], 'Amit': [34, 'Mumbai', 400013], 'Rahul': [32, 'Mumbai', 400001]}
friends = (friends1, friends2)

with open('friends.dat', 'wb') as f:
    pickle.dump(friends, f)

with open('friends.dat', 'rb') as f:
    obj = pickle.load(f)
    print(type(obj))
    print(obj)