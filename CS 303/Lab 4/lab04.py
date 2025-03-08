import random
import numpy as np
import time
import math
import sys
import csv

sys.setrecursionlimit(100000)

name = "Harrison Thomas"
blazerID = "hgthomas"

ANSI_RESET = "\u001B[0m"
ANSI_RED = "\u001B[31m"
ANSI_GREEN = "\u001B[32m"
ANSI_YELLOW = "\u001B[33m"
ANSI_BLUE = "\u001B[34m"


class HashMap:

    # defualt constructor
    # TODO: You will need to change the size for your hashmap implementation, discuss in your lab report why you need to change the hashmap size and how varying sizes affect space and time complexity
    def __init__(self):
        self.size = 2000000
        self.map = [None] * self.size
    
    #(2a): LINEAR hashing function
    def linear_put(self, key, value):
        hash = key % self.size
        while self.map[hash] != None:
            hash += 1
            if hash >= self.size:
                hash = 0
        self.map[hash] = [key,value]

    #(2b): LINEAR hashing function
    '''
    @return: returns a string representing the value associated with the search key, return None if the key is not in the hashmap
    '''
    def linear_get(self, key):
        hash = key % self.size
        while self.map[hash][0] != key:
            if self.map[hash] == None:
                return None
            hash += 1
            if hash >= self.size:
                hash = 0
        return self.map[hash][1]

    #(3a): QUADRATIC hashing function
    def quadratic_put(self, key, value):
        hash = key % self.size
        i = 1
        while self.map[hash] != None:
            hash += (i**2)
            i += 1
            if hash >= self.size:
                hash = 0
                i = 1
        self.map[hash] = [key,value]
        pass

    #(3b): QUADRATIC hashing function
    '''
    @return: returns a string representing the value associated with the search key, return None if the key is not in the hashmap
    ''' 
    def quadratic_get(self, key):
        hash = key % self.size
        i = 1
        while self.map[hash][0] != key:
            if self.map[hash] == None:
                return None
            hash += (i**2)
            i += 1
            if hash >= self.size:
                hash = 0
                i = 1
        return self.map[hash][1]

'''
@params: file_name - string input of the name of the .csv file
@params: function - string representing the put function to be used for placing elements in hashmap
@returns: returns a Hashmap object, with the Hashmap filled out using the .csv file
'''
#(4)TODO: edit the below function new_hashmap so that it reads a .csv file, and creates a hashmap using the .csv file data
# DO NOT change what has already been written
def new_hashmap(file_name, function):
    mp = HashMap()
    if (function == "linear"):
        with open(file_name, 'r') as file:
            csv_file = csv.reader(file)
            for row in csv_file:
                key = int(row[0])
                value = row[1] + " : " + row[2]
                mp.linear_put(key,value)
    else:
        with open(file_name, 'r') as file:
            csv_file = csv.reader(file)
            for row in csv_file:
                key = int(row[0])
                value = row[1] + " : " + row[2]
                mp.quadratic_put(key,value)
    return mp


############# DO NOT MODIFY CODE BELOW THIS LINE #############

print(f"Name: {ANSI_YELLOW}{name}{ANSI_RESET}")
print(f"BlazerID: {ANSI_YELLOW}{blazerID}{ANSI_RESET}")

def check_values(value1, value2):
    if (value1 != value2):
        return False
    return True

def hashmapCheckLinear(hashmap, file_name):
    passCount = 0
    failCount = 0
    is_true = False
    with open(file_name, 'r') as file:
        csv_file = csv.reader(file)
        for row in csv_file:
            key = int(row[0])
            value = row[1] + " : " + row[2]
            hashelement_value = hashmap.linear_get(key)
            is_true = check_values(value, hashelement_value)

            if is_true:
                passCount += 1
            else:
                failCount += 1

            print(f"Value at key:value {key}:\n{value} is: \n{hashelement_value}")
    return passCount > 0 and failCount == 0

def hashmapCheckQuadratic(hashmap, file_name):
    passCount = 0
    failCount = 0
    is_true = False
    with open(file_name, 'r') as file:
        csv_file = csv.reader(file)
        for row in csv_file:
            key = int(row[0])
            value = row[1] + " : " + row[2]
            hashelement_value = hashmap.quadratic_get(key)
            is_true = check_values(value, hashelement_value)

            if is_true:
                passCount += 1
            else:
                failCount += 1

            print(f"Value at key:value {key}:\n{value} is: \n{hashelement_value}")
    return passCount > 0 and failCount == 0

print(f"{ANSI_YELLOW}\n-------- Linear Hashmaps --------{ANSI_RESET}")
print(f"{ANSI_YELLOW}\n----------------------------------------{ANSI_RESET}")
print(f"{ANSI_YELLOW}Linear UPC.csv{ANSI_RESET}")
print(f"{ANSI_YELLOW}----------------------------------------{ANSI_RESET}")

linearHashmap1 = new_hashmap('UPC.csv', "linear")
start = time.time_ns()
is_true = hashmapCheckLinear(linearHashmap1, 'input.csv')
stop = time.time_ns()

print(f"\nCorrect: {ANSI_GREEN if is_true else ANSI_RED}{is_true}{ANSI_RESET} || Time: {stop-start}ns")

print(f"{ANSI_YELLOW}\n----------------------------------------{ANSI_RESET}")
print(f"{ANSI_YELLOW}Linear UPC-random.csv{ANSI_RESET}")
print(f"{ANSI_YELLOW}----------------------------------------{ANSI_RESET}")
linearHashmap2 = new_hashmap('UPC-random.csv', "linear")
start = time.time_ns()
is_true = hashmapCheckLinear(linearHashmap2, 'input.csv')
stop = time.time_ns()

print(f"\nCorrect: {ANSI_GREEN if is_true else ANSI_RED}{is_true}{ANSI_RESET} || Time: {stop-start}ns")

print(f"{ANSI_YELLOW}\n-------- Quadratic Hashmaps --------{ANSI_YELLOW}")

print(f"{ANSI_YELLOW}\n----------------------------------------{ANSI_RESET}")
print(f"{ANSI_YELLOW}Quadratic UPC.csv{ANSI_RESET}")
print(f"{ANSI_YELLOW}----------------------------------------{ANSI_RESET}")

quadraticHashmap1 = new_hashmap('UPC.csv', "quadratic")
start = time.time_ns()
is_true = hashmapCheckQuadratic(quadraticHashmap1, 'input.csv')
stop = time.time_ns()

print(f"\nCorrect: {ANSI_GREEN if is_true else ANSI_RED}{is_true}{ANSI_RESET} || Time: {stop-start}ns")

print(f"{ANSI_YELLOW}\n----------------------------------------{ANSI_RESET}")
print(f"{ANSI_YELLOW}Quadratic UPC-random.csv{ANSI_RESET}")
print(f"{ANSI_YELLOW}----------------------------------------{ANSI_RESET}")
quadraticHashmap2 = new_hashmap('UPC-random.csv', "quadratic")
start = time.time_ns()
is_true = hashmapCheckQuadratic(quadraticHashmap2, 'input.csv')
stop = time.time_ns()

print(f"\nCorrect: {ANSI_GREEN if is_true else ANSI_RED}{is_true}{ANSI_RESET} || Time: {stop-start}ns")
