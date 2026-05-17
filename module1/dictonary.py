#write a program to create a dictonary from two lists : one keys and one of values
'''
keys=["a","b","c"]
values=[1,2,3]
dic=dict(zip(keys,values))
print("dictionary",dic)
'''

#merge two dictionary into one
'''
dict1={ "a":1,"b":2}
dict2={"c":3,"d":4}
dict1.update(dict2)
print("merged dictionary :",dict1)
'''

#write a program to sort a dictonary by its values

dict3={
    "apple":50,"banana":30,"mango":40
}
sorted_dic=dict(sorted(dict3.items(),key=lambda item:item[1]))
print("sorted dictionary",sorted_dic)