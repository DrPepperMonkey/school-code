import random
import numpy as np
import time

name = "Harrison Thomas"
blazerID = "hgthomas"

#(1): LINEAR SEARCH
def linear_search(arr, x):
    for i in range(len(arr)):
        if x == arr[i]:
            return i
    return -1
 # return index of x, -1 if not found

#(2): BINARY SEARCH
def quickSort(arr:list):
        if len(arr) > 1:
            pivot, i = arr[-1], -1
            for j in range(len(arr)):
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            arr[i+1:], arr[:i] = quickSort(arr[i+1:]), quickSort(arr[:i])
        return arr
    
def binary_search(arr, low, high, x):

    mid = (high - low) // 2 #Start of search
    if x < arr[mid] and len(arr) > 1:
        return binary_search(arr[:mid],low, low + mid, x)
    if x > arr[mid] and len(arr) > 1:
        return binary_search(arr[mid:], low + mid, high, x)
    if x == arr[mid]:
        return low + mid
    else:
        return -1 # return index of x, -1 if not found

#(3): TEST FUNCTIONS
'''
params:
    arr - randomly generated array
    keys - array of integers to search for in array
    
returns:
    returns an array of indices of each key's location, -1 if key is not found
'''
def linear_search_1000(arr, keys):
    indecies = []
    for i in keys:
        indecies.append(linear_search(arr, i))
    return indecies # return an array of indices of each key

def binary_search_1000(arr, keys):
    quickSort(arr)
    indecies = []
    for i in keys:
        indecies.append(binary_search(arr,0,len(arr),i))
    return indecies # return an array of indices of each key

############# DO NOT MODIFY CODE BELOW THIS LINE #############

def gen_array(n):
    arr = np.zeros(n)
    for i in range(n):
        arr[i] = random.randint(0, n)
    return arr

print(f"Name: {name}")
print(f"BlazerID: {blazerID}")

print("------ Linear Search ------")
keys = gen_array(1000)
for n in range(4, 19):
    is_true = True
    arr = gen_array(2**n)

    start = time.time_ns()
    key_indices = linear_search_1000(arr, keys)
    stop = time.time_ns()

    for i in range(len(keys)):
        index = int(key_indices[i])
        if (index != -1) and (keys[i] != arr[index]):
            is_true = False
    
    print(f"ArraySize: 2**{n} || Correct: {is_true} || Time: {stop-start}ns")


print("------ Binary Search ------")
for n in range(4, 19):
    is_true = True
    arr = gen_array(2**n)

    start = time.time_ns()
    key_indices = binary_search_1000(arr, keys)
    stop = time.time_ns()

    for i in range(len(keys)):
        index = int(key_indices[i])
        if (index != -1) and (keys[i] != arr[index]):
            is_true = False
    
    print(f"ArraySize: 2**{n} || Correct: {is_true} || Time: {stop-start}ns")