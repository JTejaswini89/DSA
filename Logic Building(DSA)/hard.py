"""Sieve of Eratosthenes
Given a number n, find all prime numbers less than or equal to n.

Examples:

Input: n = 10
Output: [2, 3, 5, 7]
Explanation: The prime numbers up to 10 obtained by Sieve of Eratosthenes
are [2, 3, 5, 7]"""
def sieve(n):
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0 and i<n:
                break
        else:
            print(i, end=' ')

print(sieve(35))

"""Calculate the angle between hour hand and minute hand
Given a string s represents time in 24-hour format ("HH:MM"), determine
the minimum angle between the hour and minute hands of an analog clock.
Note: This problem is known as Clock angle problem.
Examples:
Input: s = "06:00"
Output: 180.000
Explanation: When the time is 06:00, the angle between the hour and minute
hands of the clock is 180.000 degrees.

The minute hand moves 6° per minute, while the hour hand moves 0.5° per minute.
Thus, the hour hand's angle is calculated as hrAngle = 30 × H + 0.5 × M, and
the minute hand's angle as minAngle = 6 × M. The difference between the
two angles is diff = |hrAngle - minAngle|."""

#this fucntion is to calculate the best angle from any two angle 
def getMin(x,y):
    return x if x<y else y
# Function to calculate the minimum angle between
# hour and minute hands
def getAngle(s): #this fucntion work is to calculate angle
    hhand=int(s[:2])
    mhand=int(s[3:])
    #convert 24 hour format to 12 hout format
    hhand=hhand%12
    #hour hand move 0.5 permintue
    hrangle=30*hhand+0.5*mhand
    #mintue hand move 6 degree permintue
    minangle=6*mhand

    #Angle
    angle=abs(hrangle-minangle)
    return getMin(360-angle,angle)
print(getAngle("06:00"))
    

"""Program for Tower of Hanoi Algorithm
Tower of Hanoi is a mathematical puzzle where we have three rods (A, B, and C)
and N disks. Initially, all the disks are stacked in decreasing value of
diameter i.e., the smallest disk is placed on the top and they are on rod A.
The objective of the puzzle is to move the entire stack to another rod
(here considered C), obeying the following simple rules:

Only one disk can be moved at a time.
Each move consists of taking the upper disk from one of the stacks and
placing it on top of another stack i.e. a disk can only be moved if it is
the uppermost disk on a stack.
No disk may be placed on top of a smaller disk.
Examples:
Input: 2
Output: Disk 1 moved from A to B
Disk 2 moved from A to C
Disk 1 moved from B to C"""

def towerofHanoi(N,from_rod,aux_rod,to_rod):
    if N==0:
        return
    towerofHanoi(N-1,from_rod,to_rod,aux_rod)
    print("MOve from",from_rod,"to rod",to_rod,"aux rod",aux_rod)
    towerofHanoi(N-1,aux_rod,to_rod,from_rod)
print(towerofHanoi(2,"A","B","C"))

"""Rat and Poisoned bottle Problem
Last Updated : 02 Jul, 2025
Given N number of bottles in which one bottle is poisoned. So the task is
to find out the minimum number of rats required to identify the poisoned bottle.
A rat can drink any number of bottles at a time and if any of the taken bottles
is poisonous, then the rat dies and cannot drink anymore.

Examples:
Input: N = 4
Output: 2
Explanation: The minimum number of rats needed to find the poisoned bottle
among 4 bottles is 2, using binary representation."""

import math
def ratpoisoned(n):
    return math.ceil(math.log2(n))
print("Minimum no of rats required are:",ratpoisoned(2))























