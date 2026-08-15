#Q1
g="13548o900"
print(g.isdigit())
#Q3
w="Wishful Thinking"
n=7
w1=w.split()
count=0
for i in w1:
  if len(i)>n:
    count+=1
print(count)
#Q4
x=23
y=54
x,y=y,x
print(x,y)
#Q5
n=int(input("Enter a number"))
if n%4==0 and n%100!=0 or n%400==0:
    print("It's a leap year")
else:
    print("Not a leap year")
#Q6
l=[2,4,6,8]
m=[3,4,5,6]
common=set(l)&set(m)
print(common)
#Q7
a=(["x",4],["y",6],["z",9])
b=dict(a)
print(b)
#Q8
from itertools import accumulate
d=[88,95,63,24,75]
e=list(accumulate(d))
print(e)
#Q10
s="ananya"
t=set(s)
count=0
max_count=0
max_char=""
for char in t:
    count=s.count(char)
    if count>max_count:
        max_count=count
        max_char=char
    print(max_count,max_char)
