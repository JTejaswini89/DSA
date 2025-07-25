"""Given a number n, check whether it is even or odd. Return true for even and false for odd.

Examples: 

Input: n = 15
Output: false
Explanation: 15 % 2 = 1, so 15 is odd .

Input: n = 44
Output: true
Explanation: 44 % 2 = 0, so 44 is even."""

#by defining the function
def is_even_odd(number):
    for i in range(1,number+1):
        if i%2==0:
            print("Even Number",i)
        else:
            print("Odd Number",i)
    return "Done"
print(is_even_odd(9))
#Using the Bitwise operator 
def isEven(n):
    if(n&1)==0:
        return "True"
    else:
        return "False"
n=15
print(isEven(n))

"""Given a number n, we need to print its table. """
def multiplication(number):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)
    return "Done"
print(multiplication(5))

"""Given a positive integer n, find the sum of the first n natural numbers.

Examples : 

Input: n = 3
Output: 6
Explanation: 1 + 2 + 3 = 6"""
#iterative basedd approach
def sum_of_naturalnos(n):
    sum=0
    x=1
    while x<=n:
        sum=sum+x
        x=x+1
    return "Iterative based",sum
print(sum_of_naturalnos(5))

#formula based(n*(n+1))/2
def sonm(n):
    return n * (n+1) // 2
print("Formula based",sonm(5))

"""Given a positive integer n, we have to find the sum of squares of first n natural numbers. 
Examples : 

Input : n = 2
Output: 5
Explanation: 1^2+2^2 = 5"""

def sumofsquares(n):
    total = 0
    for i in range(n):
        square = i ** 2
        print(i, "** 2 =", square)
        total += square
    return total

print("Total sum of squares:", sumofsquares(8))


#formula based
def sum(n):
    return (n*(n+1)*(2*n+1))/6
print(sum(8))

"""Given two numbers a and b, the task is to swap them.

Examples:

Input: a = 2, b = 3
Output: a = 3, b = 2"""
#naive prooach (uisng third variable)
a=5
b=6
print("Before Swapping")
print("a","=",a,"b","=",b)
temp=a
a=b
b=temp
print("After Swapping")
print("a","=",a,"b","=",b)

#withoput using third varabile a built-in approach
a=3
b=2
print("before swapping",a,b)
a,b=b,a
print("after swapping",a,b)

"""Given two integers n and m (m != 0). Find the number closest to n and divisible by m.
If there is more than one such number, then output the one having maximum absolute value.

Examples: 

Input: n = 13, m = 4
Output: 12
Explanation: 12 is the closest to 13, divisible by 4."""

def closest_divisible(n, m):
    # Closest multiple below or equal to n
    q = n // m
    lower = m * q

    # Closest multiple above n
    upper = m * (q + 1)

    # Return the one closer to n
    if abs(n - lower) < abs(n - upper):
        return lower
    else:
        return upper
print(closest_divisible(13, 4))  
print(closest_divisible(14, 4))

"""The dice problem
You are given a cubic dice with 6 faces. All the individual faces have a number printed on them.
The numbers are in the range of 1 to 6, like any ordinary dice. You will be provided with a face of this cube,
your task is to guess the number on the opposite face of the cube.

Examples:

Input: n = 2
Output: 5
Explanation: For dice facing number 5 opposite face will have the number 2."""
#Navie Approach(if-else way)
def oppositesideofdice(n):
    if n==1:
        return 1
    elif n==2:
        return 5
    elif n==3:
        return 4
    elif n==4:
        return 3
    elif n==5:
        return 2
    else:
        return 1
print("Using navie approach opposite side of 5 is",oppositesideofdice(5))

#Using sum of two sides
def diceside(n):
    side=7-n
    return side
print("Using two sides sum approach opposite side of 5 is",diceside(5))

"""Nth term of AP from First Two Terms
Given two integers a1 and a2, the first and second terms of an Arithmetic Series respectively, the problem is to find the nth term of the series. 
Examples :

Input : a1 = 2,  a2 = 3,  n = 4
Output : 5
Explanation : The series is 2, 3, 4, 5, 6, ....   , thus the 4th term is 5. """


#using loop
def nthTermOfAP(a1, a2, n):
    nthTerm = a1
    d = a2 - a1
    for i in range(1, n):
        nthTerm += d
    return nthTerm
a1 = 2
a2 = 3
n = 4
print("4thTermOfAP sereis (a1=2,a2=3,n=4):",nthTermOfAP(a1, a2, n))

#using formula of nth term
def nthTermOfAP(a1, a2, n):
    return a1 + (n - 1) * (a2 - a1)
a1 = 2
a2 = 3
n = 4
print("4thTermOfAPseries (a1=2,a2=3,n=4):",nthTermOfAP(a1, a2, n))












































