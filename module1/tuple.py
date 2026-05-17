# t1-->program to check whether an element exists in tuple
'''
my_tuple=(10,20,30,40)
element=20
if element in my_tuple:
    print("element exists in tuple ")
else :
    print("element not exists in tuple")
'''
#t2-->program to count the occurance of an element in a tuple
'''
new_tuple=(2,2,4,5,6,7,3,2,3)
count=0
element=2
for i in new_tuple:
    if i == element:
        count=count+1
print("occurence of element",count)
'''
# t3-->write a program to sort a list of tuple based on tuple values
'''
tuple_list =[(6,5),(4,9),(9,5)]
sort_list=sorted(tuple_list,key=lambda x:x[1])# lambda sort based on second value
print("sorted list",sort_list)
'''

# t4-->write a program to convert a tuple into a list and a list into a tuple
'''
tup1=(2,4,5,6,7,8,7)
new_tup=list(tup1)
print("tuple to list",new_tup)
li=[2,3,4,5,6]
new_li=tuple(li)
print("list to tuple",new_li)
'''