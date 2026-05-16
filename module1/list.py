# write a program to find the largest and smallest elements in a list
'''
mylist=[2,4,5,3,8]

largest=mylist[0]
smallest=mylist[0]
for i in mylist:
    if(i>largest):
        largest=i
       
    if(i<smallest):
        smallest=i
        
print("largest number=",largest)
print("smallest number=",smallest)
print(len(mylist))'''

# write a program to reverse a list without using built-in reverse functons
'''
list1=[1,2,3,4,5]
new_list=[]
for i in range(len(list1)-1,-1,-1):
   new_list.append((list1[i]))
print("reverse list",new_list)
'''
# write a program remove duplicate element from a list
"""
l2=[1,2,3,3,4,45,5,]
print("suplicate list",l2)
newlist=list(set(l2))
print("new list without duplicate",newlist)
"""
#write a rogram to count odd and even numbers
'''
l3=[1,2,3,4,5,6,7,8,9]
even_count=0
odd_count=0
for i in l3:
 if(i%2==0):
  even_count=even_count+1
 else:
  odd_count=odd_count+1
print("even number count",even_count)
print("odd number count",odd_count)

'''
# program to merge two list and sort the final list
'''
l1=[4,3,2]
l2=[1,7,4]
new_mer_l=l1+l2
print(new_mer_l)
new_mer_l.sort()
print(new_mer_l)
'''

#program to find the second largest element in a list

l1=[10,23,45,64]
l1.sort()
print("secont largest number",l1[-2])

