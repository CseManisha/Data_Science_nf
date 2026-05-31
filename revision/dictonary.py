# dictonary operation acess key value items  add update remove
import pandas as pd 
dic={
    'name':['manisha','abhishek',"ansh",'radhika'],
    'age':[23,21,0,0]

}
print(dic)
df=pd.DataFrame(dic)
print(df)
print(dic['name'])
dic["course"]=["python","java"]
print(dic)
dic.pop('age')
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())