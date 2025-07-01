import sys
#Generator function use for accessing the big content from the file and perform lazy loading in the memory


def read_largefile(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line

for line in read_largefile('bigtextRead.txt'):
    print(line.strip())