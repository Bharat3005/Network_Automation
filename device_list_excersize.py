# with open('devices.txt', 'r') as f:
#     devices =f.read().splitlines()
# my_list = list()
# for item in devices:
#     tmp = item.split(':')
#     my_list.append(tmp)
# print(my_list)

# import csv
# with open('devices.txt', 'r') as f:
#     reader = csv.reader(f, delimiter=':')
#     mylist = list()
#     for row in reader:
#         mylist.append(row)
# print(mylist)

##########################################################

# #######Excersize-1############
# with open('sample_file.txt', 'r') as f: 
#     reader = f.read().splitlines()
#     print(reader)
#     mylist = list()
# for items in reader:
#     tmp = items.split(',')
#     mylist.append(tmp)
# print(mylist)

#============================================#

# #######Excersize-2############
# def tail(file, n):
#     with open('file', 'r') as f:
# ############content is function which is read the file f and split f file into lines########
#         content = f.read().splitlines()           
# ############last is an object created for calculating the length off the contenet and -n is operator which will 
# # remove n numbers of lines from content length########
#         last = content[len(content)-n:]
#         print(last)
#         my_str = '\n'.join(last)
#         return my_str
# t = tail('samplefile.txt', 3)
# print(t)
#=========================================================#
import time
def tail(file, n):
    with open(file, 'r') as f:
        # reading the file in a list
        content = f.read().splitlines()
        # getting the last n elements of the list
        last = content[len(content)-n:]
        # print(last)
        # concateneting the list back into a string
        my_str = '\n'.join(last)
        return my_str

#  sample file: https://drive.google.com/open?id=1BHRIztTDMbiUntvwmP5is8QObuWnHrxB
while True:
    t = tail('sample_file.txt', 3)
    print(t)
    time.sleep(3)
    print('')

#=====================================================#

# def tail(file, n):
#     with open(file, 'r') as f:
#         # reading the file in a list
#         content = f.read().splitlines()
#         # getting the last n elements of the list
#         last = content[len(content)-n:]
#         # print(last)
#         # concateneting the list back into a string
#         my_str = '\n'.join(last)
#         return my_str


# t = tail('samplefile.txt', 3)
# print(t)

