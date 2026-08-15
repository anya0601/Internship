
1. Check if a string contains only digits. [X]
   -How to check if a single element is a digit?
   -How to check that?Using loop or any other way?
2. Find the median of a list of numbers. [X]
    -How to find the middle position of list.
    -How to check if the list length is odd or even.What to do if it is even?
3. Count words longer than N letters in a sentence. [X]
   - How to find the word lengths in a sentence?
   - How filter the above based on the "length" criteria.

4. Swap two variables without using a temporary variable. [X]
```
bowl_1, bowl_2 = 4,6

another_bowl =  bowl_1  # Explanantion b1 = 4, b2=6, ab =  4
bowl_1 =  bowl_2 # b1 = 6, b2 = 6, ab = 4
bowl_2 = another_bowl # b1 = 6, b2 = 4, ab = 4
```
> ```
> BOWL_1 = RICE, BOWL_2 = LENTILS
> ANYASBOWL = Pouring Rice from BOWL_1, so BOWL_1 is Empty and ANYASBOWL contains that RICE.
> BOWL_1 = Pouring LENTILS from BOWL_2, so BOWL_1 has LENTILS ATM and BOWL_2 is Empty.
> BOWL_2 = Pouring Rice from ANYASBOWL, ANYA is Bankrupt now, BOWL_1 has LENTILS and BOWL_2 has RICE.
> ```

```
Easiest Solution:

Solution 1: first, second  = second, first
> a, b, c, d, e = 1 ,2 ,3 ,4, 5
> c, d, a, b, e = a ,b ,c ,d, e

Solution 2: 
first, second = 12, 16

first = first + second # first = 28          # first = 28, second = 12
second = first - second # second = 28 - 16
first =  first - second # first = 28 - 12 = 16
```


5. Check if a given year is a leap year. [X]
   -How to check if the given year is divisible by 4.

6. Find the common elements between two lists. [X]
    -In mathematics it is done by intersection of sets does that apply here or is there another method?

~~7. Convert a list of (key, value) tuples into a dictionary. [ ]~~

8. Compute the running/cumulative sum of a list of numbers. [X]
   -How to find the sum of the number?
   -Should we use loops?

~~9. Check if a string has balanced parentheses. [ ]~~

10. Find the most frequently occurring character in a string. [X]
    -How to count the number of times the characters are appearing.
    -How to check which character has the higgest count.