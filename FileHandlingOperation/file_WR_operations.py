# #writing in file
# with open('mytextfile.text', 'w') as file:
#     file.write('Hello World')
#     file.write('\n')
#     file.write('this is a new line')
#     file.seek(0)
#
# #reading from file
# with open('mytextfile.text', 'r') as file:
#     file.seek(0)
#     for f in file:
#         print(f.strip())

#write append in file
# with open('mytextfile.txt', 'a') as file:
#     file.write("\nnext appended line")

# import csv
#
# with open('example.csv', mode='w', newline='') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(["Hello", "World"])
#     writer.writerow(["test", "32"])
#
# with open('example.csv', mode='r', newline='') as csv_file:
#     reader = csv.reader(csv_file)
#     for row in reader:
#         print(row)



data = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08'
with open('mytextfile.txt', 'wb') as myfile:
    myfile.write(data)


