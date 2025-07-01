# def check_unique(lst):
#     lstdata = []
#     # Your code goes here
#     for ls in lst:
#         if ls in lstdata:
#             print("False")
#         else:
#             lstdata.append(ls)
#     print("True")
#
# lst = [1, 2, 3, 4, 5]
# check_unique(lst)


def reverse_list(lst):
    reversed_lst = []
    data_len = len(lst)
    for i in range(len(lst)):  # loop from end to start
        if len(lst) == 0:
            return lst
        elif len(lst) == 1:
            return lst
        elif len(lst) > 0:
            reversed_lst.append(lst[data_len - 1])
            data_len = data_len - 1
    return reversed_lst

#simplest way
def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):  # loop from end to start
        reversed_lst.append(lst[i])
    return reversed_lst

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reverse_list(lst)