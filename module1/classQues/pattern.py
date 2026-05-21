# program to print tables from 2 to 5 in pattern format

start =int(input("enter starting number: "))
end=int(input("Enter ending number: "))

for i in range (start,end+1):
    print(f"\nTable of {i}")

    for j in range(1,11):
        print(f"{i}*{j} = {i*j}")
