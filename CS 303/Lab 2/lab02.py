import random
import numpy as np
import time
import math
import sys

sys.setrecursionlimit(10000)

name = "Harrison Thomas"
blazerID = "hgthomas"

#(1): SELECTION SORT
def selection_sort(arr: list):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1,len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    return arr


#(2): INSERTION SORT
def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        tmp = arr[i]
        for j in range(i-1, -1, -1):
            if tmp < arr[j]:
                arr[j + 1], arr[j] = arr[j], tmp
    return arr

#(3): MERGE SORT
def merge_sort(arr, temp, p, r):
    leftArr = []
    rightArr = []

    if len(arr) > 1:
        leftArr = merge_sort(arr[:len(arr)//2], temp, p, r)
        rightArr = merge_sort(arr[len(arr)//2:], temp, p, r)
    else:
        return arr
    
    # splits input array in half
    arr[:] = merge(leftArr,rightArr)[:]
    return arr

def merge(leftArr: list, rightArr: list): # sorts and merges two sorted arrays
    mergeArr = []
    l = 0 # left index
    r = 0 # right index

    while l < len(leftArr) and r < len(rightArr):
        if leftArr[l] < rightArr[r]:
            mergeArr.append(leftArr[l])
            l += 1
        else:
            mergeArr.append(rightArr[r])
            r +=1
    while r < len(rightArr):
        for i in range(r,len(rightArr)):
            mergeArr.append(rightArr[r])
            r += 1
        return mergeArr

    while l < len(leftArr):
        for i in range(l,len(leftArr)):
            mergeArr.append(leftArr[l])
            l += 1
        return mergeArr
    return mergeArr

'''
inputs: 
arr -> array to be sorted
p -> left index
r -> right index
'''
#(4a): QUICKSORT
def partition(arr, p, r):
    pass

def quicksort(arr, p, r):
    if len(arr) > 1:
        pivot, i = arr[-1], -1
        for j in range(len(arr)):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        i += 1
        arr[i], arr[j] = arr[j], arr[i]
        arr[i+1:], arr[:i] = quicksort(arr[i+1:], p, r), quicksort(arr[:i], p, r)
    return arr


############# DO NOT MODIFY CODE BELOW THIS LINE #############

def gen_array(n):
    arr = [0]*n
    for i in range(n):
        arr[i] = random.randint(0, n)
    return arr

def sorted_array(n):
    arr = [0]*n
    for i in range(n):
        arr[i] = i
    return arr

def reverse_sorted(n):
    arr = [0]*n
    for i in range(n):
        arr[i] = n-i
    return arr

def compare_arr(arr1, arr2):
    sorted = np.sort(arr1)
    for i in range(len(sorted)):
        if sorted[i] != arr2[i]:
            return False
    return True

print(f"Name: {name}")
print(f"BlazerID: {blazerID}")

arrays = []
for n in range(4, 17):
    arr = gen_array(2**n)
    arrays.append(arr)

print("-------- Selection Sort --------")

n = 4
for el in arrays:
    arr = el.copy()
    if (n == 4):
        print(f"Before selection sort: {arr}")
    numpy_arr = arr.copy()

    start = time.time_ns()
    selection_sort(arr)
    stop = time.time_ns()

    is_true = compare_arr(numpy_arr, arr)

    if (n == 4):
        print(f"After selection sort: {arr}")
    
    print(f"ArraySize: 2**{n} || Correct: {is_true} || Time: {stop-start}ns")
    n+=1

print("-------- Insertion Sort --------")

n = 4
for el in arrays:
    arr = el.copy()
    if (n == 4):
        print(f"Before insertion sort: {arr}")
    numpy_arr = arr.copy()

    start = time.time_ns()
    insertion_sort(arr)
    stop = time.time_ns()

    is_true = compare_arr(numpy_arr, arr)

    if (n == 4):
        print(f"After insertion sort: {arr}")
    
    print(f"ArraySize: 2**{n} || Correct: {is_true} || Time: {stop-start}ns")
    n+=1

print("-------- Merge Sort --------")

n = 4
for el in arrays:
    arr = el.copy()
    temp = [0]*len(arr)
    if (n == 4):
        print(f"Before merge sort: {arr}")
    numpy_arr = arr.copy()

    start = time.time_ns()
    merge_sort(arr, temp, 0, len(arr)-1)
    stop = time.time_ns()

    is_true = compare_arr(numpy_arr, arr)

    if (n == 4):
        print(f"After merge sort: {arr}")
    
    print(f"ArraySize: 2**{n} || Correct: {is_true} || Time: {stop-start}ns")
    n+=1

print("-------- Quicksort --------")

n = 4
for el in arrays:
    arr = el.copy()
    if (n == 4):
        print(f"Before quicksort: {arr}")
    numpy_arr = arr.copy()

    start = time.time_ns()
    quicksort(arr, 0, len(arr)-1)
    stop = time.time_ns()

    is_true = compare_arr(numpy_arr, arr)

    if (n == 4):
        print(f"After quicksort: {arr}")
    
    print(f"ArraySize: 2**{n} || Correct: {is_true} || Time: {stop-start}ns")
    n+=1

print("-------- Compare Quicksort --------")
array_types = ["random", "sorted", "reverse"]
for el in array_types:
    if el == "random":
        random1 = gen_array(5000)

        start = time.time_ns()
        quicksort(random1, 0, len(random1)-1)
        stop = time.time_ns()
        quicksort_time = stop-start

        print(f"Regular Quicksort || Array type: {el} || Time: {quicksort_time}")
    elif el == "sorted":
        random1 = sorted_array(5000)

        start = time.time_ns()
        quicksort(random1, 0, len(random1)-1)
        stop = time.time_ns()
        quicksort_time = stop-start

        print(f"Regular Quicksort || Array type: {el} || Time: {quicksort_time}")
    else:
        random1 = reverse_sorted(5000)

        start = time.time_ns()
        quicksort(random1, 0, len(random1)-1)
        stop = time.time_ns()
        quicksort_time = stop-start

        print(f"Regular Quicksort || Array type: {el} || Time: {quicksort_time}")