# list1 = [1,2,3,4,5]
# iterator = iter(list1)
# for i in iterator:
#     print(i)

list2= [5,1,2,3,4]
def generator(list2):
    for i in list2:
        yield i

#use of generator
for i in generator(list2):
    print(i)