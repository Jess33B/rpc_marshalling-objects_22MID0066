from collections import deque
n=int(input("enter no of vertex"))
e=int(input("enter the no of edges"))
graph={i : [] for i in range(n)}
print("Enter edges (u:v):")
for _ in range(e):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
#bfs
def bfs(graph,start):
    visited=set()
    queue=deque([start])
    visited.add(start)
    print("BFS Traversal:")
    while queue:
        node=queue.popleft()
        print(node,end=" ")
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
print()
#dfs
def dfs(graph,node,visited):
    visited.add(node)
    print(node,end=" ")
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph,neighbor,visited)
print()
start=int(input("enter start vertex:"))
bfs(graph,start)
print("dfs traversal:")
dfs(graph,start,set())