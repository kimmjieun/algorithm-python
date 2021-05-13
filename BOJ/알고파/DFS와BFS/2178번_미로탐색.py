# bfs 이므로 deque 사용
from collections import deque

# 이코테 미로탈출과 같은 문제
n,m = map(int,input().split()) # 세로 가로

graph = []
for _ in range(n):
    graph.append(list(map(int,input())))


# 상하좌우로 움직여야하므로
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 최단경로 문제니까 bfs
def bfs(x,y):
    queue= deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            # 허용할 수 없는 범위 이면 건너뛰기
            if nx < 0 or nx >= n or ny < 0 or ny >=m:
                continue
            # 이동할 수 없는 칸이면 건너뛰기
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]



print(bfs(0,0))