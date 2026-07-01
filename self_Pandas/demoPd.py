import pandas as pd 
# Series
a=[1,2,3,4,5]
myvar=pd.Series(a)
print(myvar)

# DataFrame
data={"name":["mani","soni","rani"],"age":[12,23,45]}

# naming the index
NewData=pd.DataFrame(data,index=["p1","p2","p3"])
print(NewData)

# access name index
#print(NewData.loc["p2"])