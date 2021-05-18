
from collections import deque
def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        start = queue.popleft()
        for n in graph[start]:
            if check[n]==0:
                check[n]=check[start]+1
                queue.append(n)

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
print(graph)
check = [0]*(n+1)
check[1]=1
bfs(1)
print(check)
res = sum([1 for t in check if 2<= t <= 3])
print(res)













