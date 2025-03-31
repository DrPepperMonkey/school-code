class DFS:

    '''
    This is the default constructor. You may add attributes or helper functions as you see fit. Make sure to update the constructor as needed.
    '''
    def __init__(self):
        pass


    '''
    Pseudocode clarifications:
    u - - vertex within G.V
    d - distance to starting vertex
    pi - neighbor in the path
    white - unvisited
    gray - in Stack
    black - visited
    '''

    '''
    This is the DFS algorithm, which takes a Graph and traverses the graph as far as possible along each path.

    @param G - graph to run DFS on
    '''
    def DFSearch(self, G):
        for i in G.getV():
            i.setColor('White')
            i.setPi(None)
        time = 0
        for i in G.getV():
            if i.getColor() == 'White':
                self.DFS_Visit(G, i, time)

    
    '''
    Takes as input a graph and a vertex, and updates the traversal time for each node. Adds adjacent vertices of u to the stack. 

    v - vertex adjacent to u

    @param G - graph DFS and DFS_Visit are being run on
    @param u - vertex being visited / discovered
    '''
    def DFS_Visit(self, G, u, time):
        time += 1
        u.setD(time)
        u.setColor('Grey')
        for i in G.getGraph()[G.getV()[u.getName()]]:
            if i.getColor() == 'White':
                i.setPi(u)
                self.DFS_Visit(G, i, time)
        u.setColor('Black')
        time += 1

    
    
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