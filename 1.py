# single source shortest path for directed acyclic graph
from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=defaultdict(list)
    def addEdge(self,u,v,w):
        self.graph[u].append((v,w))
    def topologicalSortUtil(self,v,visited,stack):
        visited[v]=True
        if v in self.graph.keys():
            for node,weight in self.graph[v]:
                if visited[node]==False:
                    self.topologicalSortUtil(node,visited,stack)
        stack.append(v)
    def shortestPath(self,s):
        visited=[False]*self.V
        stack=[]
        for i in range(self.V):
            if visited[i]==False:
                self.topologicalSortUtil(s,visited,stack)
        dist=[float("Inf")]*(self.V)
        dist[s]=0
        while stack:
            i=stack.pop()
            for node,weight in self.graph[i]:
                if dist[node]>dist[i]+weight:
                    dist[node]=dist[i]+weight
        for i in range(self.V):
            if dist[i]!=float("Inf"):
                print(f"{dist[i]}")
            else:
                print("Inf")
V=int(input("Enter the no of vertices\n"))
E=int(input("Enter the no of edges\n"))
g=Graph(V)
for i in range(E):
    u=int(input("Enter the source vertex of the edge"))
    v=int(input("Enter the destination vertex of the edge"))
    w=int(input("Enter the weight of the edge"))
    g.addEdge(u,v,w)
s=int(input("Enter the source vertex"))
print(f"following are the shortest distance from source {s}")
g.shortestPath(s)



