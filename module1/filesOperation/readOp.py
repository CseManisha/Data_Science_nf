#reading  files operation 
f=open("module1/filesOperation/demo.txt","r")
data=f.read()# read lines for multiple line reads
print(data)
line2=f.readline()# writelines for singel line read
print(line2)
line1=f.readline()
print(line1)
print(type(data))
f.close()
