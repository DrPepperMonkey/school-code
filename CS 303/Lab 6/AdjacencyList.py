from Vertex import Vertex

class AdjacencyList:

    def __init__(self, size):
        self.graph = {}
        self.V = []
        for i in range(size):
            self.V.append(Vertex(i))
            self.graph[self.V[i]] = []

    def getGraph(self):
        return self.graph
    
    def getV(self):
        return self.V

    def addEdge(self, vert1, vert2):
        self.graph[self.V[vert1]].append(self.V[vert2])
        self.graph[self.V[vert2]].append(self.V[vert1])

    
    def print(self):
        for i in range(len(self.graph)):
            print(f"{i}: ", end="")
            for j in self.graph[self.V[i]]:
                print(f"{j.name}", end=" -> ")
            print()