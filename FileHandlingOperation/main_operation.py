import os
os.getcwd()
print(os.getcwd())

with open('mytextfile.txt', 'w') as file:
   file.write("hello world i am busy there\n")
   file.write("this is another line")


with open('mytextfile.txt', 'r') as file:
    for t in file:
        print(t)

import shutil

#shutil.copy('mytextfile.txt', 'destination.txt')

import json

json_data = {'name' : 'ankit', 'age' : 34}

data = json.dumps(json_data)
print(data)
print(type(data))

json_list = json.loads(data)
print(json_list)
print(type(json_list))






