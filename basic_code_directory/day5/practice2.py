# def count_even_odd(lst):
#     # Your code goes here
#     even_counter = 0
#     odd_counter = 0
#     even_list = []
#     odd_list = []
#     for i in lst:
#
#         if i % 2 == 0:
#             even_counter = even_counter + 1
#             if i == 0:
#                 continue
#             even_list.append(i)
#         else:
#             odd_counter = odd_counter + 1
#             if i == 0:
#                 continue
#             odd_list.append(i)
#     print("Even numbers:", even_list)
#     print("Odd numbers:", odd_list)
#     print("Count of even numbers:", even_counter)
#     print("Count of odd numbers:", odd_counter)
#
#
# lst = [2,3]
# count_even_odd(lst)


def is_subset(lst1, lst2):
    return set(lst1).issubset(set(lst2))

lst1 = [1, 2, 3]
lst2 = [1, 2, 3, 4, 5]
is_subset(lst1,lst2)