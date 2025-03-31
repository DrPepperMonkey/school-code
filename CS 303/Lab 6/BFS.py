from AdjacencyList import AdjacencyList

class BFS:

    '''
    This is the default constructor. You may add attributes or helper functions as you see fit. Make sure to update the constructor as needed.
    '''
    def __init__(self):
        pass

    '''
    Pseudocode clarifications:
    u - vertex within G.V
    d - distance to starting vertex
    pi - neighbor in the path
    white - unvisited
    gray - in Queue
    black - visited
    '''

    '''
    This is the BFS algorithm, which takes a Graph and starting vertex within the graph, and updates each vertex to find the shortest path to the starting vertex

    @param G - graph to run BFS on
    @param s - starting vertex within graph
    '''
    def BFSearch(self, G, s):
        for i in G.getV():
            i.setColor('White')
            i.setD(-1)
            i.setPi(None)
        s.setColor('Grey')
        s.setD(0)
        s.setPi(None)
        Q = []
        Q.append(s)
        while len(Q) != 0:
            u = Q.pop()
            for j in G.getGraph()[G.getV()[u.getName()]]:
                if j.getColor() == 'White':
                    j.setColor('Grey')
                    j.setD(u.d + 1)
                    j.setPi(u)
                    Q.append(j)
            u.setColor('Black')

    

    '''
    Prints the path from vertex s to vertex v in graph G
    @param G - the graph
    @param s - starting vertex
    @param v - vertex to find path to from s
    '''
    def print_path(self, G, s, v):
        if v == s:
            print(s.getName())
        elif v.getPi() == None:
            print(None)
        else:
            self.print_path(G, s, v.getPi())
            print(v.getName())