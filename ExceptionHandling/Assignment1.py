# "Write a function that takes two integers as input and returns their division. Use try,
# except,and finally blocks to handle division by zero and print an appropriate message.\n",
from logging import exception

from numpy.testing.print_coercion_tables import print_new_cast_table


def takefunction(a, b):
    try:
        div =a/b
        print(div)
        return div
    except ZeroDivisionError as ex:
        print(f"Error: Cannot divide by zero.{ex}")
        return None
    finally:
        print("Execution of division operation is complete.")
takefunction(1,3)

#  "Write a function that reads the contents of a file named `data.txt`.
#  Use try, except, and  finally blocks to handle file not found errors
#  and ensure the file is properly closed.\n",

# def readfilecontent(filename):
#     try:
#         with open(filename, "r") as filedata:
#             print(filedata.read())
#     except FileNotFoundError as ex:
#         print(f"Error: Cannot find file {filename}.{ex}")
#     finally:
#         print("Execution of readfile operation is complete.")
#         filedata.close()
#
#
# readfilecontent('readme.txt')

#"Write a function that takes a list of integers and returns their sum.
# Use try, except, and finally blocks to handle TypeError
# if a non-integer value is encountered and print an appropriate message.\n",

def actionperform(filename):
    try:
        getresult = 0
        for data in filename:
            getresult += data
        print(f'Expected result: {getresult}')
    except TypeError as ex:
        print(ex)
    except Exception as ex:
        print(ex)
    finally:
        print('Execution complete.')

# #first attempt
# listdata = [1,2,"ankit",4]
# actionperform(listdata)
#

# "Write a function that prompts the user to enter an integer.
# Use try, except, and finally blocks to handle ValueError
# if the user enters a non-integer value and print an appropriate message.\n",

# #second attempt
# listdata = [1,2,"ankit",4]
# actionperform(listdata)


# "Write a function that takes a dictionary and a key as input and returns the value
# associated with the key. Use try,
# except, and finally blocks to handle KeyError
# if the key is not found in the dictionary and print an appropriate message.\n",

def dictionaryKeyFunction(samplelist, key):
    try:
        inputdata = input("Enter the input key value: ")
        for data in samplelist:
            if data.get(key) == inputdata:
                first_value = list(data.values())[1]
                print(first_value)
                return first_value
    except KeyError as ex:
        print("KeyError:", ex)
    finally:
        print('Execution complete.')

# Sample data: list of dicts
mysample = [
    {"name": "ankit", "age": 32},
    {"name": "john", "age": 28}
]

dictionaryKeyFunction(mysample, "name")