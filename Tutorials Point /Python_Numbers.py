#Python Numbers
#Absolute Value

# print(("abs(-45) : "), abs(-45))
# print(("abs(100.12) : "), abs(100.12))
# print(("abs(119L) : "), abs(119))
#======================================================#

#cile() celiling method : Python number method ceil() returns ceiling value of x - the smallest integer not less than x.

# import math
# print("math.ceil(-45.17) : ", math.ceil(-45.17))
# print("math.ceil(100.12) : ", math.ceil(100.12))
# print("math.ceil(100.72) : ", math.ceil(100.72))
# print("math.ceil(119L) : ", math.ceil(119))
# print("math.ceil(math.pi) : ", math.ceil(math.pi))
# print(math.pi)

#======================================================#

#cmp(): Python number method cmp() returns the sign of the difference of two numbers : -1 if x < y, 0 if x == y, or 1 if x > y.

# def cmp(a,b):
#     return bool(a<b) - bool(a>b) - bool(a==b)

# print ("cmp(80, 100) : ", cmp(80, 100))
# print ("cmp(180, 100) : ", cmp(180, 100))
# print ("cmp(-80, 100) : ", cmp(-80, 100))
# print ("cmp(80, -100) : ", cmp(80, -100))
# print ("cmp(80, 80) : ", cmp(80, 80))

#======================================================#

#exp(): Python number method exp() returns returns exponential of x: ex.
#fabs(): Python number method fabs() returns the absolute value of x in float.
#floor(): Python number method floor() returns floor of x - the largest integer not greater than x.
#log(): Python number method log() returns natural logarithm of x, for x > 0.


import math

print("math.exp(-45.17) : ", math.exp(-45.17))
print("math.exp(100.12) : ", math.exp(100.12))
print("math.exp(100.72) : ", math.exp(100.72))
print("math.exp(119L) : ", math.exp(119))
print("math.exp(math.pi) : ", math.exp(math.pi))

print("math.floor(-45.17) : ", math.floor(-45.17))
print("math.floor(100.12) : ", math.floor(100.12))
print("math.floor(100.72) : ", math.floor(100.72))
print("math.floor(119L) : ", math.floor(119))
print("math.floor(math.pi) : ", math.floor(math.pi))

print("math.log(100.12) : ", math.log(100.12))
print("math.log(100.72) : ", math.log(100.72))
print("math.log(119L) : ", math.log(119))
print("math.log(math.pi) : ", math.log(math.pi))
