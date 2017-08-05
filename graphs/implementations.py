"""
The following is an implementation of a directed, weighted, labeled graph with both a 2D-matrix and adjency list to
keep track of vertices, edges, and weights.

It's for illustrative purposes only- obviously it's redundant to store the same information in
BOTH data structures.
"""

class Vertex:
    def __init__(self,key):
        self.id = key
        self.adjencyList = {}

    def addNeighbor(self,nbr,weight=0):
        #insert into adjency list
        self.adjencyList[nbr] = weight

    def getConnections(self):
        return self.adjencyList.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.adjencyList[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        # self.matrix = [[-1]] #my attempt to ALWAYS have to resize it, but at least it was dynamic
        self.matrix = [[-1 for x in range(10)] for y in range(10)] # TODO make it resizeable

    def addVertex(self,key):
        # this is mostly relevant to the adjacency list
        if key in self.vertList:
            raise Exception("vertex already exists")

        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        self.numVertices = self.numVertices + 1


        """
        ALL OF THIS IS ONLY RELEVANT IF WE'RE DOING A DYNAMICALLY RESIZED MATRIX
        #expand our matrix to include the new vertex, if that vertex wasn't already in the matrix
        if key <= (len(self.matrix) -1) and key <= (len(self.matrix[0]) -1):
            print("Don't need to expand the matrix past length %d because we're adding a key %d that was already present" %(len(self.matrix), key))
        # else:
        if key > (len(self.matrix) +1) or key > (len(self.matrix[0]) +1):
            print('Key was %d but length of matrix was %d and length of matrix[0] was %d' %(key, len(self.matrix), len(self.matrix[0])))
            for n in range(len(self.matrix), key +1):
                self.matrix.append(-1) #pad the unused spots with -1
                self.matrix[0].append(-1)

            # self.printMatrix()
        """

        return newVertex

    def addEdge(self,f,t,cost=0):
        #insert into adjency list
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

        #insert into matrix
        if self.matrix[f][t] != -1:
            print("Vertex at [%d][%d] was previously set to %d" %(f, t, self.matrix[f][t]))

        self.matrix[f][t] = cost


    def getVerticesAList(self):
        return self.vertList.keys()

    def printMatrix(self):
        print("called printMatrix")
        for i in range((len(self.matrix))):
            for j in range((len(self.matrix[0]))):
                print("Row " + str(i) + " Column " + str(j) + " Edge weight " + (str(self.matrix[i][j])))

g = Graph()

for i in range(6):
    g.addVertex(i)

g.addVertex(5)

# g.printMatrix()
g.addEdge(0,1,5)
g.addEdge(5,4,8)
g.addEdge(5,4,6)
g.printMatrix()
