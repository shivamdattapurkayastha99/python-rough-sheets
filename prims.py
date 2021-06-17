from collections import defaultdict
import sys
class Heap:
    def __init__(self):
        self.array=[]
        self.size=0
        self.pos=[]
    def newminheapnode(self,v,dist):
        minheapnode=[v,dist]
        return minheapnode
    def swapminheapnode(self,a,b):
        t=self.array[a]
        self.array[a]=self.array[b]
        self.array[b]=t
    def minheapify(self,idx):
        smallest=idx
        left=2*idx+1
        right=2*idx+2
        if left<self.size and self.array[left][1]<self.array[smallest][1]:
            smallest=left
        if right<self.size and self.array[right][1]<self.array[smallest][1]:
            smallest=right
        if smallest!=idx:
            self.pos[self.array[smallest][0]]=idx
            self.pos[self.array[idx][0]]=smallest
            self.swapminheapnode(smallest,idx)
            self.minheapify(smallest)
    def extractmin(self):
        if self.isEmpty()==True:
            return
        root=self.array[0]
        lastnode=self.array[self.size-1]
        self.array[0]=lastnode
        self.pos[lastnode[0]]=0
        self.pos[root[0]]=self.size-1
        self.size-=1
        self.minheapify(0)
        return root
    def isEmpty(self):
        return True if self.size==0 else False
    def decreasekey(self,v,dist):
        i=self.pos[v]
        self.array[i][1]=dist
        while i>0 and self.array[i][1]<self.array[(i-1)//2][1]:
            self.pos[self.array[i][0]]=(i-1)//2
            self.pos[self.array[(i-1)//2][0]]=i
            self.swapminheapnode(i,(i-1)//2)
            i=(i-1)//2
    def isinminheap(self,v):
        if self.pos[v]<self.size:
            return True
        return False
def printarr(parent,n):
    for i in range(1,n):
        print(f"the vertices are {parent[i]} and {i}")
class Graph:
    def __init__(self,V):
        self.V=V
        self.graph=defaultdict(list)
    def addedge(self,src,dest,weight):
        newnode=[dest,weight]
        self.graph[src].insert(0,newnode)
        newnode=[src,weight]
        self.graph[dest].insert(0,newnode)
    def primmst(self):
        V=self.V
        key=[]
        parent=[]
        minheap=Heap()
        for v in range(V):
            parent.append(-1)
            key.append(sys.maxsize)
            minheap.array.append(minheap.newminheapnode(v,key[v]))
            minheap.pos.append(v)
        minheap.pos[0]=0
        key[0]=0
        minheap.decreasekey(0,key[0])
        minheap.size=V
        while minheap.isEmpty()==False:
            newheapnode=minheap.extractmin()
            u=newheapnode[0]
            for p in self.graph[u]:
                v=p[0]
                if minheap.isinminheap(v) and p[1]<key[v]:
                    key[v]=p[1]
                    parent[v]=u
                    minheap.decreasekey(v,key[v])
        printarr(parent,v)
n=int(input("Enter the no of vertices"))
g=Graph(n)
for i in range(n):
    u=int(input("Enter the first vertex"))
    v=int(input("Enter the second vertex"))
    w=int(input("Enter the weight of the edge"))
    g.addedge(u,v,w)
g.primmst()

        




