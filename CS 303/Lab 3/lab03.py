import random
import numpy as np
import time
import math

name = "Harrison Thomas"
blazerID = "hgthomas"

#(1): HEAP SORT
# Default constructor provided
# You may add any class attributes as you see fit to complete the assignment
# The only requirement is that the 3 functions must follow the provided pseudocode
class Heap:

    # class constructor
    def __init__(self):
        pass

    def heapsort(self, arr):
        self.buildMaxHeap(arr)
        for i in range(len(arr) - 1, -1, -1):
            arr[0], arr[i] = arr[i], arr[0]
            arr[:i] = self.maxHeapify(arr[:i],0)
        return arr

    def buildMaxHeap(self, arr):
        for i in range(len(arr)//2 -1, -1, -1):
            arr = self.maxHeapify(arr,i)
        return arr

    def maxHeapify(self, arr, i):
        max = i
        leftChild = 2*i + 1
        rightChild = 2*i + 2
        if leftChild < len(arr) and arr[leftChild] > arr[max]:
            max = leftChild
        if rightChild < len(arr) and arr[rightChild] > arr[max]:
            max = rightChild
        if max != i:
            arr[max], arr[i] = arr[i], arr[max]
            arr = self.maxHeapify(arr, max)
        return arr

#(2): MERGE AND INSERTION SORT - you may copy your lab2 solution here

# insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]
        for j in range(i-1, -1, -1):
            if tmp < arr[j]:
                arr[j + 1], arr[j] = arr[j], tmp
    return arr

# merge sort
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

def merge(leftArr, rightArr):
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

############# DO NOT MODIFY CODE BELOW THIS LINE #############

def gen_array(n):
    arr = [0]*n
    for i in range(n):
        arr[i] = random.randint(0, n)
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
    n += 1

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
    n += 1

print("-------- Heap Sort --------")

n = 4
for el in arrays:
    arr = el.copy()
    if (n == 4):
        print(f"Before heap sort: {arr}")
    numpy_arr = arr.copy()

    heap = Heap()

    start = time.time_ns()
    heap.heapsort(arr)
    stop = time.time_ns()

    is_true = compare_arr(numpy_arr, arr)

    if (n == 4):
        print(f"After heap sort: {arr}")
    
    print(f"ArraySize: 2**{n} || Correct: {is_true} || Time: {stop-start}ns")
    n += 1
