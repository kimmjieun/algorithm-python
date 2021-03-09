#런타임에러(EOFError)
# import sys
# sys.setrecursionlimit(50000) #재귀제한높이설정(기본값이상으로 안해주면 런타임에러) ※기본값:1000
#
# def dfs(x,y):
#     #주어진 범위를 벗어나는 경우에 즉시 종료
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     # 현재노드를 아직 방문하지 않았다면
#     if graph[x][y]==1:
#         #해당노드 방문처리
#         graph[x][y]=0
#         #상하좌우의 위치도 모두 재귀적으로 호출
#         dfs(x-1,y)
#         dfs(x,y-1)
#         dfs(x+1,y)
#         dfs(x,y+1)
#
#         return True
#     return False
#
# t = int(input())
# for tt in range(t):
#     n,m,k=map(int,input().split())
#
#     graph=[[0]*m for i in range(n)]
#
#     #배추밭채우기
#     for i in range(k):
#         x,y=map(int,input().split())
#         graph[x][y]=1
#     #지렁이 개수 세기
#     result=0
#     for i in range(n):
#         for j in range(m):
#             #현재위치에서 dfs수행
#             if dfs(i,j)==True:
#                 result+=1
#     print(result)

# 출력형식 맞춰주기 -> 결과를 리스트에 저장해서 나중에 한꺼번에 출력, recursionerror-> 재귀 호출횟수 제한하기
import sys
sys.setrecursionlimit(10**8) #재귀제한높이설정(기본값이상으로 안해주면 런타임에러) ※기본값:1000
def dfs(x,y):
    #주어진 범위를 벗어나는 경우에 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재노드를 아직 방문하지 않았다면
    if graph[x][y]==1:
        #해당노드 방문처리
        graph[x][y]=0
        #상하좌우의 위치도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)

        return True
    return False

def solve():
    result=0
    for i in range(n):
        for j in range(m):
            #현재위치에서 dfs수행
            if dfs(i,j)==True:
                result+=1
    print(result)

result=[]
t = int(input())
for tt in range(t):
    n,m,k=map(int,input().split())

    graph=[[0]*m for i in range(n)]

    #배추밭채우기
    for _ in range(k):
        x,y=map(int,input().split()) #y x ?

        graph[x][y]=1

    count=0
    for i in range(n):
        for j in range(m):
            #현재위치에서 dfs수행
            if dfs(i,j)==True:
                count+=1
    result.append(count)
for r in result:
    print(r)



# #음료수 얼려먹기문제 - 이것이 취업을위한 코딩테스트다
# n,m=map(int,input().split())
#
# graph=[]
# for i in range(n):
#     graph.append(list(map(int,input())))
#
# def dfs(x,y):
#     #주어진 범위를 벗어나는 경우에 즉시 종료
#     if x <= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     # 현재노드를 아직 방문하지 않았다면
#     if graph[x][y]==1:
#         #해당노드 방문처리
#         graph[x][y]=0
#         #상하좌우의 위치도 모두 재귀적으로 호출
#         dfs(x-1,y)
#         dfs(x,y-1)
#         dfs(x+1,y)
#         dfs(x,y+1)
#
#         return True
#     return False
#
# #모든 노드에 대해 음료수 채우기
# result=0
# for i in range(n):
#     for j in range(m):
#         #현재위치에서 dfs수행
#         if dfs(i,j)==True:
#             result+=1
# print(result)
