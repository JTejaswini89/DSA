"""Find k largest elements in an array
Given an array arr[] and an integer k, the task is to find k largest elements
in the given array. Elements in the output array should be in decreasing order.
Examples:

Input:  [1, 23, 12, 9, 30, 2, 50], k = 3
Output: [50, 30, 23]"""

def klargest(arr,k):
    res=sorted(arr, reverse=True) #Descending order
    return res[:k]
arr=[10,20,40,30,50,70,23,25,59,85]
k=3
print("k largest elements in the  array:",arr,"is",klargest(arr,k))

"""Kth smallest element in a row-wise and column-wise sorted 2D array
Given an n × n matrix mat[][] where each row and column is sorted in
non-decreasing order, find the kth smallest element, where k lies in the
range [1, n²].

Example:

Input:  mat[][] = [[10, 20, 30, 40],    k = 3
                             [15, 25, 35, 45],
                             [24, 29, 37, 48],
                             [32, 33, 39, 50]]
Output: 20
Explanation: The sorted order is [10, 15, 20, ...]; the 3rd element is 20."""


def ksmallest(matrix,k):
    n=len(matrix)
    arr=[]
    for i in range(n):
        for j in range(n):
            arr.append(matrix[i][j])
    arr.sort()
    print("The sorted array from the given matrix is:",arr)
    return arr[k-1]
matrix=[[10, 20, 30, 40],   
        [15, 25, 35, 45],
        [24, 29, 37, 48],
        [32, 33, 39, 50]]
k=5#returns element at the index four as in array indexing start with 0
print("Kth smallest element in a row-wise and column-wise sorted 2D array:",
      ksmallest(matrix,k))


"""Floor in a Sorted Array
Given a sorted array and a value x, find the element of the floor of x.
The floor of x is the largest element in the array smaller than or equal to x.
Examples:

Input: arr[] = [1, 2, 8, 10, 10, 12, 19], x = 5
Output: 1
Explanation: Largest number less than or equal to 5 is 2, whose index is 1"""


def floorsorted(arr, x):
    floor_index = -1
    for i in range(len(arr)):
        if arr[i] <= x:
            floor_index = i
        else:
            break  # since array is sorted, no need to check further
    return floor_index

arr = [1, 2, 8, 10, 10, 12, 19]
x = 5
print(floorsorted(arr, x))


"""Ceiling in a sorted array
Given a sorted array and a value x, find index of the ceiling of x.
The ceiling of x is the smallest element in an array greater than or equal to x.
Note: In case of multiple occurrences of ceiling of x, return the index of the
first occurrence.

Examples : 

Input: arr[] = [1, 2, 8, 10, 10, 12, 19], x = 5
Output: 2
Explanation: Smallest number greater than 5 is 8, whose index is 2."""


def ceilingsort(array, x):
    for i in range(len(array)):
        if array[i] >= x:
            return i
    return -1  # No ceiling exists

arr = [1, 2, 8, 10, 10, 12, 19]
x = 5
print(ceilingsort(arr, x))


"""Bitonic Point - Maximum in Increasing Decreasing Array
Given an array arr[] of integers which is initially strictly increasing and
then strictly decreasing, the task is to find the bitonic point, that is the
maximum value in the array. 
Note: Bitonic Point is a point in bitonic sequence before which elements are
strictly increasing and after which elements are strictly decreasing.

Examples: 

Input: arr[] = [1, 2, 4, 5, 7, 8, 3]
Output: 8"""

def bitonicpoint(arr):
    n=len(arr)
    mx=arr[0]
    for i in range(1,n):
        if arr[i]>mx:
            mx=arr[i]
        else:
            break
    return mx
print("Bitonic Point - Maximum in Increasing Decreasing Array:",bitonicpoint([1, 2, 4, 5, 7, 8, 3]))























