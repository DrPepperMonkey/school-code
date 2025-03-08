import numpy as np
import random

def gen_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 20))
    return arr

def insertSort(arr: list):
    for i in range(1, len(arr)):
        tmp = arr[i]
        for j in range(i-1, -1, -1):
            if tmp < arr[j]:
                arr[j + 1], arr[j] = arr[j], tmp
    return arr
        
def selectSort(arr: list):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1,len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    return arr

def bubbleSort(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j + 1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def mergeSort(arr: list):
    leftArr = []
    rightArr = []
    if len(arr) > 1:
        leftArr = mergeSort(arr[:len(arr)//2])
        rightArr = mergeSort(arr[len(arr)//2:])
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
 
def radixSort(arr):
    max = arr[0]
    k = 0
    for i in arr:
        if i > max:
            max = i
    while max != 0:
        max = max // 10
        k += 1

    for j in range(k,1,-1):
        for l in range(len(arr)):
            ''

'''    
leftChild = 2*i + 1
rightChild = 2 * i + 2
parent = i//2 - 1
'''

def buildMaxHeap(arr: list) -> list:
    for i in range(len(arr)//2 -1, -1, -1):
        heapify(arr,i)
    return arr

def heapify(arr: list, i):
    max = i
    leftChild = 2*i + 1
    rightChild = 2*i + 2
    if leftChild < len(arr) and arr[leftChild] > arr[max]:
        max = leftChild
    if rightChild < len(arr) and arr[rightChild] > arr[max]:
        max = rightChild
    if max != i:
        arr[max], arr[i] = arr[i], arr[max]
        heapify(arr, max)
    return arr

def heapSort(arr: list):
    buildMaxHeap(arr)
    for i in range(len(arr) - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        arr[:i] = heapify(arr[:i], 0)
    return arr


def sortChoice(arr: list):
    print('Choose a sorting method')
    print('[0]: Selection Sort \n' + 
            '[1]: Insertion Sort \n' +
            '[2]: Bubble Sort \n' +
            '[3]: Merge Sort \n' +
            '[4]: Quick Sort \n' +
            '[5]: Radix Sort \n' +
            '[6]: Heap Sort \n' +
            '[7]: Quit')
    choiceIn = int(input())

    match choiceIn:
        case 0:
            print('---Selection Sort---')
            return selectSort(arr.copy())
        case 1:
            print('---Insertion Sort---')
            return insertSort(arr.copy())
        case 2:
            print('---Bubble Sort---')
            return bubbleSort(arr.copy())
        case 3:
            print('---Merge Sort---')
            return mergeSort(arr.copy())
        case 4:
            print('---Quick Sort---')
            return quickSort(arr.copy())
        case 5:
            print('---Radix Sort---')
            return radixSort(arr.copy())
        case 6:
            print('---Heap Sort---')
            return heapSort(arr.copy())
        
def compare(arr1: list, arr2: list) -> bool:
    return arr1 == arr2

def main():
    testArray = gen_array(20)
    print(sortChoice(testArray.copy()))
    print(compare(sortChoice(testArray.copy()), sortChoice(testArray.copy())))

main()
