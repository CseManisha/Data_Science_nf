#reading  files operation r with
'''
f=open("module1/filesOperation/demo.txt","r")
data=f.read()# read lines for multiple line reads
print(data)
line2=f.readline()# writelines for singel line read
print(line2)
line1=f.readline()
print(line1)
print(type(data))
f.close()
'''

#read r with
'''
with open("module1/filesOperation/demo.txt","r")as f:
     data=f.read()
     print(data)
'''

# with  w
'''
with open("module1/filesOperation/demo.txt","w") as f:
     f.write("hi  i am learning pthon")
'''
# deleting the file 
'''

import os
os.remove("module1/filesOperation/sample.txt")
'''

# practice  cerate a file practice.txt using python add the same line 
"""   
hi everyone
we are learning file i/o
using pyhon
i like programming in java 
"""
'''
with open("module1/filesOperation/practic.txt","w")as f:
    f.write(" hii everyone")
    f.write("\n we are learning file i/o")
    f.write("\n using pyhon")
    f.write("\n i like programming in java")
'''

'''
# replace string
with open("module1/filesOperation/practic.txt","r")as f:
    data=f.read()
    newData=data.replace("java","pyhton")
    print(newData)
# override newdata with old data
with open("module1/filesOperation/practic.txt","w")as f:
    f.write(newData)
'''
'''
def check_for_word():
 word="learning"
 with open("module1/filesOperation/practic.txt","r")as f:
  data=f.read()
  if(data.find(word) != -1):
   print("found")
  else:
   print("not found")
check_for_word() 
#searching a word in with line number
def check_for_line():
 word="X"
 data=True
 line_no=1
 with open("module1/filesOperation/practic.txt","r")as f:
  while data:
   data=f.readline()
   if(word in data):
     print(line_no)
     return
   line_no +=1
 return -1

print(check_for_line())
'''

# numbers even or not
with open("module1/filesOperation/numb.txt","r")as f:
    data=f.read()
    print(data)