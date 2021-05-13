# from collections import deque
# t = int(input())
#
# dx = [-2,-1,+1,+2,-2,-1,+1,+2]
# dy = [-1,-2,-2,-1,+1,+2,+2,+1]
#
# def bfs(x,y):
#     count = 0
#     queue = deque()
#     queue.append((x,y))
#     while queue:
#         x,y = queue.popleft()
#
#         for i in range(8):
#
#
#             nx = x+dx[i]
#             ny = y+dy[i]
#
#             if nx < 0 or nx >= I or ny < 0 or ny >= I :
#                 continue
#             if nx != end_x and ny != end_y:
#
#                 continue
#
#             if nx == end_x and ny == end_y:
#                 break
#
#     return count
#
# for _ in range(t):
#     I = int(input())
#     start_x,start_y = map(int,input().split())
#     end_x,end_y = map(int,input().split())
#
#     print(bfs(start_x,start_y))

# def dfs(x,y):
#     if x < 0 or x >= I or y < 0 or y <= I :
#         return False
#     if x != end_x and y != end_y:
#         return False
#     count += 1
#     dfs(x-2, y-1)
#     dfs(x-1, y-2)
#     dfs(x+1, y-2)
#     dfs(x+2, y-1)
#     dfs(x-2, y+1)
#     dfs(x-1, y+2)
#     dfs(x+1, y+2)
#     dfs(x+2, y+1)
#
#
#     if x == end_x and y == end_y:
#         return True
#
# global count
# for _ in range(t):
#     I = int(input())
#     start_x,start_y = map(int,input().split())
#     end_x,end_y = map(int,input().split())
#     count =0
#     if dfs(start_x,start_y) == True:
#         print(count)
#



from collections import deque
t = int(input())

dx = [-2,-1,+1,+2,-2,-1,+1,+2]
dy = [-1,-2,-2,-1,+1,+2,+2,+1]

def bfs(sx,sy,ex,ey):
    queue = deque()
    queue.append((sx,sy))
    s[sx][sy]=1

    while queue:
        x,y = queue.popleft()
        if x ==ex and y ==ey:
            print(s[ex][ey]-1)
            return

        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<I and 0<=ny<I and s[nx][ny]==0:
                queue.append((nx,ny))
                s[nx][ny]=s[x][y]+1


for _ in range(t):
    I = int(input())
    start_x,start_y = map(int,input().split())
    end_x,end_y = map(int,input().split())
    s = [[0]*I for i in range(I)]
    bfs(start_x,start_y,end_x,end_y)




























