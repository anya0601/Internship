#Q5
n=int(input("Enter a number"))
if n%4==0 and n%100!=0 or n%400==0:
    print("It's a leap year")
else:
    print("Not a leap year")
#Q6
l=[2,4,6,8]
m=[3,4,5,6]
n=l&m
print(n)