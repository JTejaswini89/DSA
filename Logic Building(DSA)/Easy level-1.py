"""Given a number n, find the sum of its digits.
Examples : 
Input: n = 687
Output: 21
Explanation: The sum of its digits are: 6 + 8 + 7 = 21"""
#Digit Extraction
n=156
total=0
while n>0:
    rem=n%10
    total+=rem
    n=n//10
print("Digit Extraction",total)

#Recursive based approach
def totalvalue(n):
    if n==0:
        return 0
    return n%10+totalvalue(n//10)#Recursive case
print("Recursive based approach",totalvalue(153))

#string conversion
n=123
ori=str(n)
total=0
for ch in ori:
    total+=int(ch)
print("string conversion",total)

"""Given an Integer n, find the reverse of its digits.
Examples:  
Input: n = 122
Output: 221
Explanation: By reversing the digits of number, number will change into 221."""
#Digit Extraction
n=143
total=0
while n>0:
    rem=n%10
    total=total*10+rem
    n=n//10
print(total)

#String conversion
n=145
ori=str(n)
print(ori[::-1])

"""Given a positive integer, check if the number is prime or not.
A prime is a natural number greater than 1 that has no positive divisors other
than 1 and itself. Examples of the first few prime numbers are {2, 3, 5, ...}
Examples : 
Input:  n = 11
Output: true"""

n=10
for i in range(1,n):
    for j in range(2,i):
        if i%j==0:
            print("Not Prime",i)
    else:
        print("Prime",i)

#For a single value
n = 10
is_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print(n ,"is Prime")
else:
    print(n,"is Not Prime")


"""You are given two coordinates (x1, y1) and (x2, y2) of a
two-dimensional graph. Find the distance between them.

Examples: 

Input : x1, y1 = (3, 4)
           x2, y2 = (7, 7)
Output : 5"""

import math
x1,y1=(3,4)
x2,y2=(7,7)
distance=math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))
print(distance)

"""heck whether triangle is valid or not if sides are given
Given three sides, check whether triangle is valid or not. 
Examples:  
Input :  a = 7, b = 10, c = 5 
Output : Valid
We can draw a triangle with the given three edge lengths.

Approach: A triangle is valid if sum of its two sides is greater than
the third side. If three sides are a, b and c, then three conditions should
be met. 
(a + b) > c
(a + c) > b
(b + c) > a  """

a,b,c=1,10,12
if (a+b)>c and (a+c)>b and(b+c)>a:
    print("Valid triangle")
else:
    print("not valid")

"""Factorial of a Number
Last Updated : 23 Jul, 2025
Given the number n (n >=0), find its factorial. Factorial of n is defined as 1 x 2 x ... x n. For n = 0, factorial is 1. We are going to discuss iterative and recursive programs in this post.

Examples:

Input: n = 5
Output: 120
Explanation: 5! = 5 * 4 * 3 * 2 * 1 = 120"""

def factorial(n):
    if n==0:
        return 1
    elif n<0:
        return "Enter a valid a number"
    else:
        result = 1
        while n > 1:
            result *= n
            n -= 1
        return result
print(factorial(5))

#Recursive absed approach
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print(fact(5))

"""Pair Cube Count
Given n, count all 'a' and 'b' that satisfy the condition a^3 + b^3 = n.
Where (a, b) and (b, a) are considered two different pairs

Examples: 

Input: n = 9
Output: 2
Explanation: 1^3 + 2^3 = 9 and 2^3 + 1^3 = 9"""

def cubecount(n):
    count=0
    for i in range(1,n+1):
        for j in range(n+1):
            if i**3+j**3==n:
                count+=1
    return count
print("There are no of valid pairs:",cubecount(9))

"""Perfect Number
A number is a perfect number if it is equal to the sum of its proper divisors,
that is, the sum of its positive divisors excluding the number itself.
Find whether a given positive integer n is perfect or not.
Examples: 

Input: n = 15
Output: false
Explanation: Divisors of 15 are 1, 3 and 5. Sum of divisors is 9
which is not equal to 15."""

def perfectnumber(n):
    total=0
    for i in range(1,n):
        if n%i==0:
            total+=i
    return total==n
print(perfectnumber(6))
    
"""Program to add two fractions
Given two integer arrays a[] and b[] containing two integers each
representing the numerator and denominator of a fraction respectively.
The task is to find the sum of the two fractions and return the numerator
and denominator of the result.

Examples : 

Input:  a = [1, 2] , b = [3, 2] 
Output: [2, 1] 
Explanation: 1/2 + 3/2 = 2/1"""

a=[1,2]
b=[3,2]
numerator=a[0]*b[1]+b[0]*a[1]
denominator=a[1]*b[1]
print([numerator//denominator])

"""Find day of the week for a given date
Given a date (day, month, year), the task is to determine the day of the week on which that date falls. The function should be able to compute the day for any date in the past or future. The function should return values from 0 to 6 where 0 means Sunday, 1 Monday and so on.

Examples:

Input: d = 30, m = 8, y = 2010
Output: 1
Explanation: 30th August 2010 was a Monday."""

def day_of_week(d,m,y):
    month_code=[6,2,2,5,0,3,5,1,4,6,2,4]#predefined month codes
    if m<3:
        y-=1
    year_code=(y%100)+(y%100)//4#year code calculation
    year_code=year_code+(y//100)//4+5*(y*100)%7#centurt year code 
    return (d+month_code[m-1]+year_code)%7#day of the week formula
print(day_of_week(15,6,1995))
# Output the result as an integer (0 = Sunday, 1 = Monday, ..., 6 = Saturday)

"""Fibonacci"""

n=5
n0=0
n1=1
for i in range(n):
    nthterm=n0+n1
    n0,n1=n1,nthterm
    print(n0)
print("n0:",n0,"n1:",n1,"nthterm:",nthterm)

#recursive method
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(10))

"""Armstrong number"""
num = 153
n = num  # preserve original number
total = 0
sum_of_powers = len(str(n))
while n>0:
    rem=n%10
    total+=rem**sum_of_powers
    n=n//10
print("Sumof poweered number",total)

if total==num:
    print(num,"is a armstrong")
else:
    print(num,"not a armstrong")


def armstrong(number):
    total=0
    n=number
    sum_of_p=len(str(n))
    while n>0:
        rem=n%10
        total+=rem**sum_of_p
        n=n//10
    if total==num:
        print( "Armstrong")
    else:
        print("not a armstrong")
print(armstrong(123))








