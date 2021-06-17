import sys
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[[0 for column in range(vertices)]for row in range(vertices)]
    def printSolution(self,dist):
        print("Vertex\tDistance from source ")
        for node in range(self.V):
            print(f"{node}\t{dist[node]}")
    def minDistance(self,dist,sptSet):
        min=sys.maxsize
        global minindex
        for v in range(self.V):
            if dist[v]<min and sptSet[v]==False:
                min=dist[v]
                minindex=v
        return minindex
    def dijshtra(self,src):
        dist=[sys.maxsize]*self.V
        dist[src]=0
        sptSet=[False]*self.V
        for cout in range(self.V):
            u=self.minDistance(dist,sptSet)
            sptSet[u]=True
            for v in range(self.V):
                if self.graph[u][v]>0 and sptSet[v]==False and dist[v]>dist[u]+self.graph[u][v]:
                    dist[v]=dist[u]+self.graph[u][v]
        self.printSolution(dist)
n=int(input("Enter the no of vertices"))
g=Graph(n)

g.graph=[[int(input("Enter the edge weights of the graph"))for j in range(n)]for i in range(n)]

g.dijshtra(0)

        