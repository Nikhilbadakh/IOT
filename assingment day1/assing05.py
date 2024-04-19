# Using for loop, write and run a Python program to find factorial from 0 to
#10.
fact=1
count=fact

li=[1,2,3,4,5,6,7,8,9,10]

for value in li:
    while fact<=value:
        count=count*fact
        fact=fact+1
    else:
        print(f"the factorial is {value} is{count}")

