#"Write a function that reads the
# contents of a file named `sample.txt` and prints each line.\n"),

with open('sample.txt', 'r') as file:
    for line in file:
        print(line.strip())  #strip  to avoid  the spaces in between the lines

import os
currect_directory = os.getcwd()
print(currect_directory)