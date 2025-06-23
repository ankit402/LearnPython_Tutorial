import os
cwd = os.getcwd()
print(cwd)

new_directory="newdir"
# os.mkdir(new_directory)
# print(f"Directory{new_directory}")

#listing files
item = os.listdir('.')
print(item)

file_name= "test.txt"
# full_path = os.path.join(new_directory, file_name)
# print(full_path)


# if os.path.isfile(file_name):
#     print("file is there in the directory")
# elif os.path.isdir(new_directory):
#     print("directory is there in the directory")
# else:
#     print("both file and directory are not there")

#gettting the absolute path
relative_path = 'example.txt'
abs= os.path.abspath(relative_path)
print(abs)
