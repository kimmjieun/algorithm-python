from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
m = int(input())
adj = [[] for i in range(n + 1)]
result = [0 for i in range(n + 1)]
def bfs(start):
    q = deque()
    q.append(start)
    visit = [0 for i in range(n + 1)]
    visit[start] = 1
    while q:
        d = q.popleft()
        for i in adj[d]:
            if visit[i] == 0:
                visit[i] = 1
                result[i] = result[d] + 1
                q.append(i)
for i in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
bfs(a)
print(result[b] if result[b] != 0 else -1)