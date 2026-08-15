# Q2
# Solution 1
data = [3,4,5]         
is_odd = len(data)%2!=0
median = data[int(len(data)/2)] if is_odd else (data[int(len(data)/2)] + data[int(len(data)/2) + 1])/2
print(median)

# solution 2
data = [3,4,5]
is_odd = len(data)%2!=0
if is_odd:
    middle_index = len(data)//2
    median = data[middle_index]
else: 
    middle_index1 = len(data)//2 - 1
    middle_index2 = len(data)//2
    median = (data[middle_index1] + data[middle_index2]) / 2
#Q5
n = 2000 #int(input("Enter a number"))
if n%4==0 and n%100!=0 or n%400==0:
    print("It's a leap year")
else:
    print("Not a leap year")
#Q6
l=[2,4,6,8]
m=[3,4,5,6]
# Find the common elements in both : 
# i.e., set intersection operatation where 
# each of the lists will be a set and python 
# has a built-in set data structure that can be 
# used to find the common elements between two 
# lists. Here's how you can do it:

set_l = set(l)
set_m = set(m)
common = set_l.intersection(set_m)
print(common)

# Q7
my_list = [("Name", "Anya"), ("Age", 25), ("City", "New York")]
my_dict = dict(my_list)
print(my_dict)

# Q8
from itertools import accumulate
my_list = [1,2,3,4,5,6,7]
print(f"Running sum of the list: {list(accumulate(my_list))}")

# Q10

print("___10_____")
my_str = "ananya" #input("Enter a string: ")
unique_chars = set(my_str)
print(unique_chars)
max_count = 0
max_char = ''
for individual_char in unique_chars:
    count = my_str.count(individual_char)
    if count > max_count:
        max_count = count
        max_char = individual_char

print(f"Character '{max_char}' appears {max_count} times.")