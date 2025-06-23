
# def mycounter():
#     with open('mytextfile.txt', 'r') as myfile:
#         lines = myfile.readlines()
#         line_count = len(lines)
#         word_count = sum(len(line.split()) for line in lines)
#         char_count = sum(len(line) for line in lines)
#     return line_count, word_count, char_count
#
# lines, words, char = mycounter()
# print(f"lines:{lines} words:{words} char:{char} ")
word_count = 0
with open('mytextfile.txt' , 'r') as myfile:
    for line in myfile:
        word_count += len(line.split())
    for line in myfile.readlines():
        line_length = len(line)

