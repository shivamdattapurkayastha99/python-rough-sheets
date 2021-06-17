class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[]
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
    def printArr(self,dist):
        print("Vertex distance from source")
        for i in range(self.V):
            print(f"{i}\t{dist[i]}")
    def belmanford(self,src):
        dist=[float("Inf")]*self.V
        dist[src]=0
        for i in range(self.V-1):
            for u,v,w in self.graph:
                if dist[u]!=float("Inf") and dist[u]+w<dist[v]:
                    dist[v]=dist[u]+w
        for u,v,w in self.graph:
            if dist[u]!=float("Inf") and dist[u]+w<dist[v]:
                print("Graph contains -ve weight cycle")
                return
        self.printArr(dist)
n=int(input("Enter the no of vertices"))
g=Graph(n)
nEdges=int(input("Enter the no of edges"))
for i in range(nEdges):
    u=int(input("Enter the first vertex"))
    v=int(input("Enter the second vertex"))
    w=int(input("Enter the edge weight"))
    g.addEdge(u,v,w)
g.belmanford(0)



