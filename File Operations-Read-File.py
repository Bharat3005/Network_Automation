# f = open('configuration.txt', 'r')
# content = f.read(10)
# content = f.read(5)
# print(content)
# print(content)
# f.close()
# print(f.closed)

# with open('configuration.txt', 'r') as file:
#     print(file.read())
#     print(file.closed)


# ## Opening the file in read only mode
# f = open('a.txt', 'r')
 
# ## Move the cursor on position 4 inside the file
# f.seek(4)
 
# ## Read 5 characters starting with position 4 and return them in variable called word
# word = f.read(5)
# print(word)
 
# ## Closing the file
# f.close()

# with open('configuration.txt', 'r') as file:
#     my_list = file.readlines()
#     print(my_list) 

with open('configuration.txt', 'r') as file:
    for line in file:
        print(line, line.strip('\n'))
        