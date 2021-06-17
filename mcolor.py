# mcoloring or graph coloring problem using backtracking
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[[0 for column in range(vertices)]for row in range(vertices)]
        

    def isSafe(self,v,color,c):
        for i in range(self.V):
            if self.graph[v][i]==1 and color[i]==c:
                return False
        return True
    def graphcoloringutil(self,m,color,v):
        if v==self.V:
            return True
        for c in range(1,m+1):
            if self.isSafe(v,color,c)==True:
                color[v]=c
                if self.graphcoloringutil(m,color,v+1)==True:
                    return True
                color[v]=0
    def graphcoloring(self,m):
        color=[0]*self.V
        if self.graphcoloringutil(m,color,0)==None:
            return False
        print("Solution exists and the assigned colors are:")
        for c in color:
            print(c)
        return True
n=int(input("Enter the no of vertices"))
g=Graph(n)
g.graph=[[]]

g.graph=[[int(input("Enter 0 if there is not an edge and 1 for an edge ")) for j in range(n)] for i in range(n)]
        
m=int(input("Enter the no of colors with which the graph can be colored "))
g.graphcoloring(m)


