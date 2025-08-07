"""Duplicates within K distance
k = 3
arr = [1, 2, 3, 4, 1, 2, 3, 4]
Duplicate of 1 is at index 0 and 4 → |0 - 4| = 4 (> 3)

Duplicate of 2 is at index 1 and 5 → |1 - 5| = 4

Duplicate of 3 is at index 2 and 6 → |2 - 6| = 4

Duplicate of 4 is at index 3 and 7 → |3 - 7| = 4

Since no duplicate is within distance ≤ 3, answer is 'No'.
"""

def duplicatesdistance(arr,k):
    last_ele={}
    for i,num in enumerate(arr):
        if num in last_ele:
            if i-last_ele[num]<=k:
                return "yes"
        last_ele[num]=i
    return "No"
print(duplicatesdistance([1, 2, 3, 4, 1, 2, 3, 4],3))


"Generate the sum of all sub arrays"""
def sum_of_subarrays(arr):
    n=len(arr)
    res=[]
    total=0
    for i in range(n):
        for j in range(i,n):
            res=arr[i:j+1]
            total+=sum(res)
    return total
print(sum_of_subarrays([1,2,3,4]))

"""Stock Buy and Sell - Multiple Transaction Allowed
Given an array prices[] of size n denoting the cost of stock on each day, the task is to find the maximum total profit if we can buy and sell the stocks any number of times.

Note: We can only sell a stock which we have bought earlier and we cannot hold multiple stocks on any day.

Examples:

Input: prices[] = {100, 180, 260, 310, 40, 535, 695}
Output: 865 """
def stockbuy(arr):
    profit=0
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            profit+=arr[i]-arr[i-1]
            print("Buy on",str(i-1),"Sell on",str(i),
                  "Profit is:",arr[i]-arr[i-1])
arr=[100,180,260,310,40,535,695]
print(arr)
print(stockbuy([100,180,260,310,40,535,695]))

"""Unique Number I
Given an array of integers, every element in the array appears twice except
for one element which appears only once. The task is to identify and return
the element that occurs only once.

Examples: 

Input:  arr[] = [2, 3, 5, 4, 5, 3, 4]
Output: 2 """
def unique(arr):
    res=[]
    count=0
    for i in arr:
        if arr.count(i)==1 and i  not in res:
            res.append(arr[i])
            print(i)
        if count==2:
            break
print(unique([2, 3, 5, 4, 5, 3, 4,6]))


"""Find the Missing Number
Given an array arr[] of size n-1 with distinct integers in the range of [1, n].
This array represents a permutation of the integers from 1 to n with one
element missing. Find the missing element in the array.

Examples: 

Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
Output: 6
"""
def missingnumber(arr):
    n=len(arr)+1
    total=sum(arr)
    expectedsum=(n*(n+1))//2
    missing=expectedsum-total
    return missing
print(missingnumber([8, 2, 4, 5, 3, 7, 1]))

"""Missing and Repeating in an Array
Given an unsorted array arr[] of size n, containing elements from the range 1 to n, it is known that one number in this range is missing, and another number occurs twice in the array, find both the duplicate number and the missing number.
Examples: 
Input: arr[] = [3, 1, 3]
Output: [3, 2]"""

def missing_and_repeating(arr):
    seen = set()
    repeating = -1
    n = len(arr)
    for i in arr:
        if i in seen:
            repeating = i
        else:
            seen.add(i)

    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(arr)
    missing = expected_sum - (actual_sum - repeating)

    return [repeating, missing]

print(missing_and_repeating([3, 1, 3]))











    
