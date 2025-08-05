"""Alternate elements of an array
Given an array arr[], the task is to print every alternate element of the array
starting from the first element.

Examples:
Input: arr[] = [10, 20, 30, 40, 50]
Output: 10 30 50"""
def alternate(arr):
    res=[]
    for i in range(0,len(arr),2):
        res.append(arr[i])
    return res
arr=[10,20,30,40,50]
print(alternate(arr))

"""Leaders in an array
Given an array arr[] of size n,the task is to find all the Leaders in the array.
An element is a Leader if it is greater than or equal to all the elements to
its right side.

Note: The rightmost element is always a leader.
Examples:

Input: arr[] = [16, 17, 4, 3, 5, 2]
Output: [17 5 2]
Explanation:17 is greater than all the elements to its right i.e., [4, 3, 5, 2], therefore 17 is a leader. 5 is greater than all the elements to its right
i.e., [2], therefore 5 is a leader. 2 has no element to its right,
therefore 2 is a leader."""

def leader(arr):
    res=[]
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]<arr[j]:
                break
        else:
             res.append(arr[i])
    return res
print(leader([16, 17, 4, 3, 5, 2]))

"""Check if an Array is Sorted
Given an array arr[], check if it is sorted in ascending order or not.
Equal values are allowed in an array and two consecutive equal values are
considered sorted.
Examples: 
Input: arr[] = [10, 20, 30, 40, 50]
Output: true
Explanation: The given array is sorted."""

def sort(arr):
    arr1=arr
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr==arr1
print("The sorted array is:",sort([10,30,20,50,40]))

"""Remove duplicates from Sorted Array
Given a sorted array arr[] of size n, the goal is to rearrange the array so
that all distinct elements appear at the beginning in sorted order.
Additionally, return the length of this distinct sorted subarray.

Note: The elements after the distinct ones can be in any order and hold any
value, as they don't affect the result.

Examples: 

Input: arr[] = [2, 2, 2, 2, 2]
Output: [2]"""


def duplicates(arr):
    unique=[]
    n=len(arr)
    for i in range(n):
        if arr[i] not in unique:
            unique.append(arr[i])
    return unique
print(duplicates([1,2,2,3,4,5,5,6]))
print(len(arr))


"""Generate all the subarrays of a list"""
def subarrays(arr):
    n=len(arr)
    res=[]
    for i in range(n):
        for j in range(i,n):
            res.append(arr[i:j+1]) #using slicing 
    return res
print(subarrays([1,2,3]))


"""Reverse an array"""
arr=[1,2,3,4,5]
reversed_arr=arr[::-1]
print("The original array is:",arr)
print("The reversed array:",reversed_arr)

#Using loopin statements
array=[10,20,30,40,50]
rev_arr=[]
for i in range(len(array)-1,-1,-1):
    rev_arr.append(array[i])
print(rev_arr)



























