"""Fraction to Recurring Decimal
Given two integers a and b(b != 0), the task is to return the fraction a/b
in string format.If the fractional part is repeating, enclose the repeating
part in parentheses.
Examples: 
Input: a = 1, b = 2
Output: "0.5"
Explanation: 1/2 = 0.5 with no repeating part.

Input: a = 50, b = 22
Output: "2.(27)"
Explanation: 50/22 = 2.27272727... Since fractional part (27) is repeating,
it is enclosed in parentheses."""


def fractioToDecimal(a,b)->str:
    if a==0:
        return "0"
    result=[]
    if (a<0)^(b<0):
        result.append("-")
    a,b=abs(a),abs(b)
    #integer part
    int_part=a//b
    result.append(str(int_part))
    remainder=a%b
    if remainder==0:
        return "".join(result)
    result.append(".")
    remainder_map={}
    while remainder!=0:
        if remainder in remainder_map:
            index=remainder_map[remainder]
            result.insert(index,"(")
            result.append(")")
            break
        remainder_map[remainder]=len(result)
        remainder*=10
        digit=remainder//b
        result.append(str(digit))
        remainder%=b
    return "".join(result)
print(fractioToDecimal(a=50,b=22))


"""Program to calculate the value of nPr
Given two numbers, n and r, the task is to compute nPr, which represents
the number of ways to arrange r elements from a set of n elements.
It is calculated using the formula n!/(n−r)!, where "!" denotes the
factorial operation.
                          nPr = n! / (n - r)! 
Examples:

Input: n = 5 r = 2
Output: 20
Explanation: 5P2 = 5! / (5 - 2)!  = 20"""


def factorial(n):
    result=1
    for i in range(2,n+1):
        result*=i
    return result
def npr(n,r):
    return factorial(n)//factorial(n-r)
print(npr(5,2))
        
"""Program to calculate value of nCr
Given two numbers n and r, The task is to find the value of nCr .
Combinations represent the number of ways to choose r elements from a set of
n distinct elements, without regard to the order in which they are selected.
The formula for calculating combinations is :
                        nCr = n! / r!(n - r)! 
Note: If r is greater than n, return 0.
Examples
Input: n = 5, r = 2
Output: 10 
Explanation: The value of  5C2 is calculated as 5! / ((5−2)! * 2!​)= 10."""
def fact(n):
    result=1
    for i in range(2,n+1):
        result*=i
    return result
def ncr(n,r):
    if r>n:
        return 0
    return fact(n)//(fact(r)*fact(n-r))
print(ncr(5,2))


"""Program to Print Pascal's Triangle
Given an integer n, the task is to find the first n rows of Pascal's triangle.
Pascal's triangle is a triangular array of binomial coefficients."""

def pascalTriangle(n):
    triangle=[]
    for row_num in range(n):
        row=[1]
        if row_num>0:
            pre=triangle[-1]
            for i in range(1,row_num):
                value=pre[i-1]+pre[i]
                row.append(value)
            row.append(1)
        triangle.append(row)
    return triangle
print(pascalTriangle(5))

"""Find all factors of a Positive Number
Given a positive integer n, find all the distinct divisors of n.
Examples:
Input: n = 10       
Output: [1, 2, 5, 10]
Explanation: 1, 2, 5 and 10 are the divisors of 10. 

Input: n = 100
Output: [1, 2, 4, 5, 10, 20, 25, 50, 100]
Explanation: 1, 2, 4, 5, 10, 20, 25, 50 and 100 are divisors of 100."""

def factors(n):
    res=[]
    for i in range(1,n+1):
        if n%i==0:
            res.append(i)
    return res
print(factors(10))


"""Prime Factor Program
Given an integer n, find all unique prime factors of n.
A prime factor is a prime number that divides n exactly
(without leaving a remainder).
Examples:
Input: n = 100
Output: [2, 5]
Explanation: Unique prime factors of 100 are 2 and 5.
Input: n = 60
Output: [2, 3, 5]
Explanation: Prime factors of 60 are 2, 2, 3, 5.
Unique prime factors are 2, 3 and 5."""

def prime_factors(n):
    res = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            res.append(i)
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        res.append(n)  # n is prime
    return res
print(prime_factors(100))


"""Modular Exponentiation (Power in Modular Arithmetic)
Given three integers x, n, and M, compute (xn) % M
(remainder when x raised to the power n is divided by M).
Examples : 
Input:  x = 3, n = 2, M = 4
Output: 1
Explanation: 32 % 4 = 9 % 4 = 1.

Input:  x = 2, n = 6, M = 10
Output: 4
Explanation: 26 % 10 = 64 % 10 = 4."""

def modularExponent(x,n,M):
    res=1
    for _ in range(n):
        res=(x**n)%M
    return res
print(modularExponent(3,2,4))




































































