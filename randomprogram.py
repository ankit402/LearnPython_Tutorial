import random
mylist = ["apple", 'banana', 'graps']
r = random.choice(mylist)
print(r)

#high level operations on the file collection
import shutil

#shutil.copyfile('myfile.txt', 'mynew2.txt')

#data serialization
import json

data = {
    'name' : "ankit",
    'age' : 32
}

json_str = json.dumps(data)
print(json_str)
print(type(json_str))

json_revert = json.loads(json_str)
print(json_revert)
print(type(json_revert))