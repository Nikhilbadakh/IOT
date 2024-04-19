#  4] Write a Python function to find the maximum of three numbers.





def maximum(a, b, c): 
 
    if (a >= b) and (a >= c): 
        maximum = a 
        print(f"maximum={a}")

 
    elif (b >= a) and (b >= c): 
        maximum = b 
        print(f"maximum={b}")

    else: 
        maximum= c 
        print(f"maximum={c}")

         
    return maximum

a= float(input("Enter the 1st integer no :"))
b= float(input("Enter the 2nd integer no :"))
c= float(input("Enter the 3rd integer no :"))
maximum(a,b,c)


