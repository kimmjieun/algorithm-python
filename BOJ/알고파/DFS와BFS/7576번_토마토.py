from collections import deque
m,n = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
# a = [list(map(int, input().split())) for i in range(n)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]

de = deque()

def bfs():
    while len(de)!=0:
        x,y = de.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==0:
                    graph[nx][ny]=graph[x][y]+1
                    de.append([nx,ny])

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            de.append([i,j])
bfs()

z = 1
result =-1

for i in graph: # 모두 익었는지 확인
    for j in i:
        if j==0:#j가 0이면 익지않은것
            z=0
        result = max(result,j)

if z ==0: # 모두 익지못한 상태
    print(-1)
elif result ==1: # 모두 익어있던 상태
    print(0)
else:
    print(result-1)#최소날짜