#Write a Python function to calculate the factorial of a number (a non-negative integer). The function acc
#epts the number as an argument.

def factorial(num1):
    factorial=1

    if num1 < 0:
       print("Sorry, factorial does not for negative")
    elif num1 == 0:
     print("The factorial of 0 is 1")
    else:
      for i in range(1,num1 + 1):
       factorial = factorial*i
    print("The factorial of",num1,"is",factorial)

    return(num1)


num1=int(input("Enter the integer for find factorial:"))
factorial(num1)


