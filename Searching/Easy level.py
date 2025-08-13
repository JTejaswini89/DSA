"""Largest element in an Array
Given an array arr. The task is to find the largest element in the given array. 
Examples: 

Input: arr[] = [10, 20, 4]
Output: 20
Explanation: Among 10, 20 and 4, 20 is the largest. """

def sorting(arr):
    return max(arr)
print(sorting([52,25,40,60]))
#======================================
def search(arr):
    res=sorted(arr)
    return res[-1]
print(search([10, 20, 4]))
#======================================
def sort(arr,n):
    mx=arr[0]

    for i in range(1,n):
        if arr[i]>mx:
            mx=arr[i]
    return mx
arr=[10,5,20,25]
n=len(arr)
print(sort(arr,n))


"""Second Largest Element in an Array
Given an array of positive integers arr[] of size n, the task is to find
second largest distinct element in the array.
Note: If the elements does not exist, return -1.

Examples:

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34"""

def secondlargest(arr):
    n=len(arr)
    largest=-1
    secondlargest=-1
    if n==0:
        return -1
    for i in range(1,n):
        if arr[i]>largest:
            largest=arr[i]
    for i in range(1,n):
        if arr[i]>secondlargest and arr[i]!=largest:
            secondlargest=arr[i]
    return secondlargest
print("Second Largest Element in an Array:",secondlargest([10,20,50,40,80,90]))

#====================================================
def builtin(arr):
    res=sorted(arr)
    secondlargest=res[-2]
    return secondlargest
print("Built-In method usage:",builtin([10,20,30,40,50,70]))



"""Largest three distinct elements in an array
Given an array arr[], the task is to find the top three largest distinct
integers present in the array.
Note: If there are less than three distinct elements in the array, then
return the available distinct numbers in descending order.

Examples :

Input: arr[] = [10, 4, 3, 50, 23, 90]
Output: [90, 50, 23]"""

def get3largest(arr):
    frst=sec=thrd=int()
    n=len(arr)
    for i in range(1,n):
        if arr[i]>frst:
            thrd=sec
            sec=frst
            frst=arr[i]
        elif arr[i]>sec and arr[i]!=frst:
            thrd=sec
            sec=arr[i]
        elif arr[i]>thrd and arr[i]!=sec and arr[i]!=sec:
            thrd=arr[i]
    res=[]
    if frst==int():
        return res
    res.append(frst)

    if sec==int():
        return sec
    res.append(sec)
    if thrd==int():
        return thrd
    res.append(thrd)
    return res
print("Largest three distinct elements in an array:",get3largest([10,20,30,40,50,90,70,100,56]))


    
"""Find the first repeating element in an array of integers
Given an array of integers arr[], The task is to find the index of first
repeating element in it i.e. the element that occurs more than once and whose
index of the first occurrence is the smallest. 

Examples: 

Input: arr[] = {10, 5, 3, 4, 3, 5, 6}
Output: 5 """

def repeatingelement(arr,n):
    n=len(arr)
    for i in range(1,n):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                return arr[i]
    return -1
arr=[10,2, 3, 4, 3, 5, 6,3]
n=len(arr)
index=repeatingelement(arr,n)
if index==-1:
    print("No repeating elements")
else:
    print("The first repeating element in an array of integers",index)


"""Missing and Repeating in an Array
Given an unsorted array arr[] of size n, containing elements from the range 1
to n, it is known that one number in this range is missing, and another number
occurs twice in the array, find both the duplicate number and the missing
number.
Examples: 

Input: arr[] = [3, 1, 3]
Output: [3, 2]"""

def miss_and_repeating(arr):
    n=len(arr)
    #actual sum
    s=sum(arr)
    p=sum(x*x for x in arr)

    #expected sum
    sn=n*(n+1)//2
    pn=(n*(n+1)*(2*n+1))//6

    #differnce of actual sum with expected sum
    diff=s-sn
    #difference of acutal squared sum and expected squared sum
    sq_diff=p-pn

    #solve for Difference and Missing
    sum_dm=sq_diff//diff

    #calculate the duplicate
    duplicate=(diff+sq_diff)//2
    missing=duplicate-diff
    return [duplicate,missing]
print("Missing and Repeating in an Array:",miss_and_repeating([3,1,3]))


"""Count 1's in a sorted binary array
Given a binary array arr[] of size n, which is sorted in non-increasing order, count the number of 1's in it. 

Examples: 

Input: arr[] = [1, 1, 0, 0, 0, 0, 0]
Output: 2"""

def count_ones(arr):
    count=0
    for num in arr:
        if num==1:
            count+=1
        else:
            pass
    return count
print(count_ones([1,1,0,1,0,0,0,1,0,0,0]))


"""Find k largest elements in an array
Given an array arr[] and an integer k, the task is to find k largest elements in the given array. Elements in the output array should be in decreasing order.

Examples:

Input:  [1, 23, 12, 9, 30, 2, 50], k = 3
Output: [50, 30, 23]"""


def klargest(arr, k):
    # sort the given array in descending order
    arr.sort(reverse=True)
    # store the first k elements in result list
    res = arr[:k]
    return [res]
    
arr = [1, 23, 12, 9, 30, 2, 50]
k = 3
res = klargest(arr, k)
print(' '.join(map(str, res)))























    

