# m,n,k = map(int,input().split())
#
# graph = [[0]*n for i in range(m)]
#
# for _ in range(k):
#     x1,y1,x2,y2= map(int,input().split())
#     for i in range(y1,y2):
#         for j in range(x1,x2):
#             graph[i][j] = 1
#
#
# def dfs(x, y):
#     global count  # 함수속에서 나온 count값을 밖에서 쓰기위해
#     # 주어진 범위를 벗어나는 경우에 즉시 종료
#     if x <= -1 or x >= m or y <= -1 or y >= n:
#         return False
#     # 현재노드를 아직 방문하지 않았다면
#     if graph[x][y] == 0:
#         count += 1
#         # 해당노드 방문처리
#         graph[x][y] = 1
#         # 상하좌우의 위치도 모두 재귀적으로 호출
#         dfs(x - 1, y)
#         dfs(x, y - 1)
#         dfs(x + 1, y)
#         dfs(x, y + 1)
#         return True
#     return False
#
#
# result = 0
# count = 0
# danji = []
# result = 0
# for i in range(n):
#     for j in range(m):
#         # 현재위치에서 dfs수행
#         if dfs(i, j) == True:
#             result += 1
#             danji.append(count)
#             count = 0
#
# print(result)
# danji.sort()  # 디폴트 오름차순
# for d in danji:
#     print(d,end=' ')

from collections import deque

m,n,k = map(int,input().split())

graph = [[0]*n for i in range(m)]

for _ in range(k):
    x1,y1,x2,y2= map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            graph[i][j] = 1

dx = [-1, 1, 0, 0] # 좌 우 상 하
dy = [0, 0, 1, -1] # 좌 우 상 하


def bfs(i,j):
    queue = deque() # 영역시작좌표를 queue에 넣어준다
    queue.append((i,j))
    graph[i][j]=1 # 다시 방문하지 않기 위해 1로 변경
    cnt=1
    while queue :
        now = queue.popleft()
        x,y = now[0],now[1]
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if (0 <= nx < m) and (0 <= ny < n):
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    queue.append((nx, ny))
                    cnt += 1
    return cnt

area = 0 # 영역의 개수
cnts = [] # 영역의 넓이
for i in range(m):
    for j in range(n):
        if graph[i][j]==0:
            cnts.append(bfs(i,j))
            area+=1
print(area)
cnts.sort()
print(*cnts)