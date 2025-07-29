"""Given a positive integer n, find its square root.
If n is not a perfect square, then return floor of √n.
Examples : 
Input: n = 4
Output: 2
Explanation: The square root of 4 is 2."""

def squareroot(n):
    res=1
    while res*res<=n:
        res+=1
    return res-1
print("Square root of 11 is(after floor the root value):",squareroot(11))

#Built in mehtod
import math
def sqrtroot(n):
    res=int(math.sqrt(n))
    return res
print("Square root of 4 is:",sqrtroot(4))


"""Given a number, the task is to check if a number is divisible by 4 or not.
The input number may be large and it may not be possible to store even if we use long long int.

Examples:

Input : n = 1124"""
n=20
if n%4==0:
    print(n,"Divisible by four")
else:
    print(n,"Not Divisible by four")


"""Given a number in the form of string s, Check if the number is divisible
by 11 or not. The input number may be large and it may not be possible to store it even if we use long long int.

Examples: 

Input: s = "76945"
Output: true
Explanation: s when divided by 11 gives 0 as remainder."""
n=145623
if n%11==0:
    print(n,"Divisble by Eleven")
else:
    print(n,"Not divisible by Eleven")

#Another way of finding
def divisiblebyeleven(n):
    odd_digit=0
    even_digit=0
    for i in range(len(n)):
        digit=int(n[i])
        if digit%2==1:
            odd_digit+=digit
        else:
            even_digit+=digit
    return (odd_digit-even_digit)%11==0
print(divisiblebyeleven("12345"))
    
"""Given a number s represented as a string, determine whether the
integer it represents is divisible by 13 or not.

Examples : 

Input: s = "2911285"
Output: true
Explanation: 2911285 / 13 = 223945, which is a whole number with no remainder."""
    

n=156
if n%13==0:
    print(n,"Divisble by 13")
else:
    print(n,"Not divisble by 13")

"""Given three numbers a, b and k, find k-th digit in ab from right side

Examples: 
Input : a = 3, b = 3, k = 1
Output : 7
Explanation: 3^3 = 27 for k = 1. First digit is 7 in 27"""

a=3
b=5
k=2
res=a**b
last=[]
for i in range(k):
    last_digit=res%10
    last.append(last_digit)
print(res)
print(last)

"""Given two integers a and b(b != 0), the task is to return the fraction a/b in string format. If the fractional part is repeating, enclose the repeating part in parentheses.

Examples: 

Input: a = 1, b = 2
Output: "0.5"
Explanation: 1/2 = 0.5 with no repeating part."""

a=5
b=4
res=a/b
num="res"

after=[()]
for i in num:
    if i is not unique:
        after.append(i)
print(res,after)

















