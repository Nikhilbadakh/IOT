#2] Write a program to accept a 4 digit number and
#a. Display face value of each decimal digit
#b. Display place value of each decimal digit
#c. Display no in reverse order by changing decimal place values If user enters a 4 digit number 9361 outp
#ut should be
#a. 9 3 6 1
#b. 9361 = 9 000 + 300 + 60 + 9
#c. 1639

n=int(input("Enter 4 digit number :"))
a=int(n/10)
b=int(n/10%10)
c=int(n/100%10)
d=int(n/1000)

print(d,c,b,a,'\n')
print(f"{n}={d*1000}+{c*100}+{b*10}+{a}\n")
print(a,b,c,d,'\n')