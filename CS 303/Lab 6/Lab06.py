import random
import numpy as np
import time
import math
import sys
from BFS import BFS
from DFS import DFS
from Vertex import Vertex
from AdjacencyList import AdjacencyList

sys.setrecursionlimit(100000)

name = "Harrison Thomas"
blazerID = "hgthomas"

print(f"Name: {name}")
print(f"BlazerID: {blazerID}")


# TODO: Call/test your adjacency list representation of tinyG.txt here
print("-------- Adjacency List Graphs ---------")
def toGraph(file: str):

    with open(file, 'r', encoding='UTF8') as f:
        lines = f.readlines()
        graph = AdjacencyList(int(lines[0]))

        for i in range(2, len(lines)):
            edge = lines[i].split()
            graph.addEdge(int(edge[0]), int(edge[1]))

        f.close()
        return graph

tinyG = toGraph('tinyG.txt')
mediumG = toGraph('mediumG.txt')
tinyG.print()
'mediumG.print()'
    

# TODO: Call/test your BFS implementations for tinyG and mediumG below
print("-------- BFS TinyG.txt --------")
start1 = time.time_ns()

# TODO: Call BFS here
tinyBFS = BFS()
tinyBFS.BFSearch(tinyG, tinyG.getV()[0])
end1 = time.time_ns()
# TODO: Print the BFS path
for i in range(len(tinyG.getV())):
    print(f'----{i}----')
    tinyBFS.print_path(tinyG, tinyG.getV()[0], tinyG.getV()[i])
    print()
print("-------- BFS MediumG.txt --------")
start2 = time.time_ns()

# TODO: Call BFS here
medBFS = BFS()
medBFS.BFSearch(mediumG, mediumG.getV()[0])
end2 = time.time_ns()
# TODO: Print the BFS path
for i in range(len(mediumG.getV())):
    print(f'---{i}---')
    medBFS.print_path(mediumG, mediumG.getV()[0], mediumG.getV()[i])
    print()
# TODO: Call/test your DFS implementations for tinyG and mediumG here
print("-------- DFS TinyG.txt --------")
start3 = time.time_ns()

# TODO: Call DFS here
tinyDFS = DFS()
tinyDFS.DFSearch(tinyG)
end3 = time.time_ns()
# TODO: Print the DFS path
for i in range(len(tinyG.getV())):
    print(f'---{i}---')
    tinyDFS.print_path(tinyG, tinyG.getV()[0], tinyG.getV()[i])
    print()
print("-------- DFS MediumG.txt --------")
start4 = time.time_ns()

# TODO: Call DFS here
medDFS = DFS()
medDFS.DFSearch(mediumG)
end4 = time.time_ns()
# TODO: Print the DFS path
for i in range(len(mediumG.getV())):
    print(f'---{i}---')
    medDFS.print_path(mediumG, mediumG.getV()[0], mediumG.getV()[i])
    print()
print(f"BFS tinyG.txt: {end1-start1}ns")
print(f"BFS mediumG.txt: {end2-start2}ns")
print(f"DFS tinyG.txt: {end3-start3}ns")
print(f"DFS mediumG.txt: {end4-start4}ns")