#given two sets,check if one set is subset of another
'''
set1={1,2,3}
set2={1,2,3,4,5}
if set1.union(set2):
    print("set1 is a subset of set2")
else:
    print("not a subset")
    '''

#write a program to check wheather  two lists have at least one common element using sets
list1=[1,2,3,4,5]
list2=[4,5,6,4]
common = set(list1)&set(list2)
if(common):
    print("commen element",common)
else:
    print("no element commen")