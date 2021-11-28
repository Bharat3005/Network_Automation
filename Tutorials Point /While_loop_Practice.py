# count = 0
# while (count < 9):
#     print(f'The output is less than:', count)
#     count = count + 1 
# print('You have crack the code')

#=================================================================#
# The infinite loop

#!/usr/bin/python

# var = 1
# while var == 1 :  # This constructs an infinite loop
#    num = input('Enter the number: ')
#    print("You entered: ", num)

# print("Good bye!")
#===================================================================#

#The Else statement

# count = 0
# while (count < 9):
#     print(f'The output is less than:', count)
#     count = count + 1
# else: 
#     print(count , 'is not less than:', 9)


# flag = 1 
# while (flag): print('Given flag is true')
# print('Good Bye')

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

numbers = [10,15,24,36,47,55,62]
index = 0
x = 0
while index < len(numbers):
    x = numbers[index]
    if  x % 2 == 0:
               print(x)
    index += 1