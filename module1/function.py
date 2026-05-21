# question on function

'''
1-->create a function to check wheather two strings are anagrams----problem
 write a function that accepts two strings and returns true if both are anagrams, otherwise false.
'''
"""
def is_anagram(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()

    return sorted(str1)==sorted(str2)

print(is_anagram("manish","aanishm"))
"""

'''
2-->create a function to find second largest number in a list
problem--
write a function that accepts a list and returns the second largest number
'''
'''
def s_largest_num(list1):
    list1.sort()
    s_num=list1[-2]
    return s_num
print(s_largest_num([2,4,5,6,7]))
'''
''' 
3--->create a function to count vowels in a sentences
problem
write a function that accepts a sentences and returns the count of each vowel
'''
'''def vowel_count(sentence):
    vowels=('aeiou')
    result={}# empty dictonary
    for vowels in vowels:
        result[vowels]=sentence.lower().count(vowels)
    return result
print(vowel_count(" i am python"))'''

'''
4-->create a function to check wheather a number is an armstrong number
problem
write a function that returns true if a number is an Armstrong number
'''
'''def is_armstrong(number):# 153 is 1**3,+,5**3,+,3**3==153 
    num_str=str(number)
    power=len(num_str)
    total=0

    for digit in num_str:
        total=total+int(digit)**power
    return total==number
print(is_armstrong(151))'''

'''
5-->create a function to find common elements between multiple lists
problem
write a function that three lists and returns common elements.
'''
def comm_elem(list1,list2,list3):
    new_list=set(list1).intersection(set(list2) & set(list3))
    return list(new_list)
print(comm_elem([1,2,3,4],[2,3,4],[2,3,]))
