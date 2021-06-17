from collections import defaultdict
class graph:
    def __init__(self,vertices):
        self.graph=defaultdict(list)
        self.V=vertices
    def addedge(self,u,v):
        self.graph[u].append(v)
    def topologicalsortutils(self,v,visited,stack):
        visited[v]=True
        for i in self.graph[v]:
            if visited[i]==False:
                self.topologicalsortutils(i,visited,stack)
        stack.insert(0,v)
    def topologicalsort(self):
        visited=[False]*self.V
        stack=[]
        for i in range(self.V):
            if visited[i]==False:
                self.topologicalsortutils(i,visited,stack)
        print(stack)
g=graph(6)
g.addedge(5,2)
g.addedge(5,0)
g.addedge(4,0)
g.addedge(4,1)
g.addedge(2,3)
g.addedge(3,1)
g.topologicalsort()



