import random
import numpy as np
import time
import math
import sys
from node import Node
import csv

sys.setrecursionlimit(100000)

name = "Harrison Thomas"
blazerID = "hgthomas"

class BST:

    def __init__(self):
        self.root = None
        self.array = [None]
    
    #(1): TREE INSERT
    '''
    @params: Tree - BST Tree
    @params: z - Node object to be inserted
    '''
    def treeInsert(self, Tree, z):
        if Tree.treeSearch(0[0],z[0]) == None:
            ...

        



    #(2): IN ORDER TREE WALK
    # prints the elements (keys) of the BST in an in-order format (correct = sorted)
    # x = starting node
    def inOrderTraversal(self, x):
        pass

    #(3): TREE SEARCH
    # x = starting node
    # k = key you are searching for
    def treeSearch(self, x, k):
        if self.array[x] == k:
            return x
        elif self.array[x] < k:
            self.treeSearch((2*x)+1, k)
        elif self.array[x] > k:
            self.treeSearch((2*x)+2, k)
        return None
        pass # returns the node with the corresponding key = k

'''
@params: file_name - string input of the name of the .csv file
@returns: returns a BST object, with the BST filled out using the .csv file
'''
#(4)TODO: edit the below function new_BST so that it reads a .csv file, and creates a BST using the .csv file data
# DO NOT change what has already been written
def new_BST(file_name):
    with open(file_name, 'r') as file:
        csv_file = csv.reader(file)
        tree = BST()
        for row in csv_file:
            key = int(row[0])
            value = row[1] + " : " + row[2]
    return -1

############# DO NOT MODIFY CODE BELOW THIS LINE #############

print(f"Name: {name}")
print(f"BlazerID: {blazerID}")

def check_values(value1, value2):
    if (value1 == value2):
        return True
    return False

def BST_check(tree, file_name):
    is_true = False
    with open(file_name, 'r') as file:
        csv_file = csv.reader(file)
        for row in csv_file:
            key = int(row[0])
            value = row[1] + " : " + row[2]
            tree_node = tree.treeSearch(tree.root, key)
            is_true = check_values(value, tree_node.value)

            print(f"Key : value at key: {key} is {tree_node.key} : {tree_node.value}")
    return is_true

print("-------- BST 'UPC-random.csv' --------")

tree = new_BST("UPC-random.csv")

print("In order traversal")
tree.inOrderTraversal(tree.root)

print("BST Search")
start = time.time_ns()
is_true = BST_check(tree, 'input.csv')
stop = time.time_ns()

print(f"\nCorrect: {is_true} || Time: {stop-start}ns")

print("-------- BST 'UPC.csv' --------")

tree2 = new_BST("UPC.csv")
tree.inOrderTraversal(tree.root)

print("BST Search")
start = time.time_ns()
is_true = BST_check(tree, 'input.csv')
stop = time.time_ns()

print(f"\nCorrect: {is_true} || Time: {stop-start}ns")