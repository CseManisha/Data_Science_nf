'''
i=1
while i<=5:
    print(i)
    i=i+1
'''
'''
num=int(input("enter the number="))
while num%2==0:
 print("num is even")
 num=num+1 
'''
'''
num=int(input("enter number "))
while num<=10:
    print(num)
    num=num+1

'''
'''
num=int(input("reverse num="))
while num>=1:
 print(num)
 num=num-1
'''
# num=int(input("even number 1 to 20="))
# while num<=20:
#     if num%2==0:
#      print(num)
#     num=num+1

# i=2
# while i<=20:
#    print(i)
#    i=i+2
# print("all number is done")
print("check number in list")
num=[2,4,6,7,8]
i=0
digit=6
while i<len(num):
 if(digit==num[i]):
    print(" number found",num[i],"found at index ",i)
    break
 i=i+1
else:
  print("number not found")


