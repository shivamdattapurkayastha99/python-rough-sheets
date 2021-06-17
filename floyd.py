# V=4
INF=999
def floyd(graph,V):
    # dist=map(lambda  i: map(lambda j: j,i),graph)
    dist=[[graph[i][j] for j in range(V)]for i in range(V)]
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
    printSolution(dist,V)
def printSolution(dist,V):
    print("the shortest distance between every pair of vertices")
    for i in range(V):
            for j in range(V):
                if dist[i][j]==INF:
                    print(f"{INF}")
                else:
                    print(f"{dist[i][j]}")
                if j==V-1:
                    print("")
V=int(input("Enter the no of vertices"))
graph=[[int(input("Enter 999 for infinity and enter the distances for finite distance"))for j in range(V)]for i in range(V)]
floyd(graph,V)

