# def multiple(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError as ex:
#          print(f'exception{ex}')
#
# test = multiple(1,0)
# print(test)
from fontTools.misc.cython import returns

# try:
#     a=b
# except NameError as ex:
#     print(ex)


try:
    num = int(input("enter the number"))
    result = 10/num
except ValueError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(result)
finally:
    print(f"finally")
