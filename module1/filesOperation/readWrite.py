# r+ a+ w+ operations in file handling
# read +write no teuncate
'''f=open("module1/filesOperation/readWrite.txt","r+")
f.write("mani")
f.close()
'''
#write read truncate
'''
f=open("module1/filesOperation/readWrite.txt","w+")
print(f.read())
f.write("abc")
f.close()
'''
# a+ append and read no truncate
f=open("module1/filesOperation/readWrite.txt","a+")
print(f.read())
f.write("hii mani")
f.close()