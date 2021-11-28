def word_count(file):
    with open('wc.txt', 'r') as f:
        content = f.read().splitlines()
        lines = len(content)
        words = 0 
        for line in content: 
            words += len(line.split())

        chars = 0 
        for chars in content:
                chars += len(list(line())
        return lines, words,chars

print(word_count('wc.txt'))


# def wc(file):
#     with open(file, 'r') as f:
#         # reading the file into a list
#         content = f.read().splitlines()

#         lines = len(content)

#         words = 0
#         for line in content:
#             words += len(line.split())

#         chars = 0
#         for line in content:
#             chars += len(list(line))

#         return lines, words, chars

# print(wc('sample_file.txt'))