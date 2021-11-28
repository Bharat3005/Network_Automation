import json
with open('friends.json', 'rt') as f:
    obj = json.load(f)
    print(type(obj))
    print(obj)

json_string = """[
    {
        "Bharat": [
            26,
            "Mumbai",
            410206
        ],
        "Pragati": [
            24,
            "Mumbai",
            400612
        ],
        "Shailesh": [
            26,
            "Mumbai",
            400043
        ]
    },
    {
        "Durgesh": [
            24,
            "Mumbai",
            410216
        ],
        "Amit": [
            34,
            "Mumbai",
            400013
        ],
        "Rahul": [
            32,
            "Mumbai",
            400001
        ]
    }
]
"""
obj = json.loads(json_string)
print(type(obj))
print(obj)










#################################
## Data Serialization and Deserialization with JSON
#################################
 
import json
 
# Declaring a dictionary
friends = {"Dan": (20, "London", 13242252), "Maria":[25, "Madrid", 34232424]}
 
 
# Serializing the dictionary to a text file called `friends.json`
with open('friends.json', 'wt') as f:
    json.dump(friends, f, indent=4)
 
 
# Serializing the dictionary to a JSON encoded string
json_string = json.dumps(friends, indent=4)
print(json_string)
 
# Deserializing from file into a Python Object
with open('friends.json') as f:
    obj = json.load(f)
 
    print(type(obj))  # => dict
    print(obj)        # => friends = {"Dan": (20, "London", 13242252), "Maria":[25, "Madrid", 34232424]}
 
 
# Loading a JSON encoded string intro a Python Object
json_string = """{
    "Dan": [
        20,
        "London",
        13242252
    ],
    "Maria": [
        25,
        "Madrid",
        34232424
    ]
}"""
 
obj = json.loads(json_string)
print(type(obj))    # => dict
print(obj)          # => friends = {"Dan": (20, "London", 13242252), "Maria":[25, "Madrid", 34232424]}
