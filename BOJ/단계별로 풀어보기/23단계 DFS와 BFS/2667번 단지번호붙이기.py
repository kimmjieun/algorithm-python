# #음료수 얼려먹기문제 - 이것이 취업을위한 코딩테스트다
# n=int(input())
#
# graph=[]
# for i in range(n):
#     graph.append(list(map(int,input())))
#
# def dfs(x,y):
#     #주어진 범위를 벗어나는 경우에 즉시 종료
#     if x <= -1 or x >= n or y <= -1 or y >= n:
#         return False
#     # 현재노드를 아직 방문하지 않았다면
#     if graph[x][y]==0:
#         #해당노드 방문처리
#         graph[x][y]=1
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
#     for j in range(n):
#         #현재위치에서 dfs수행
#         if dfs(i,j)==True:
#             result+=1
# print(result)

# 2667번
n=int(input())

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))



def dfs(x,y):
    global count  # 함수속에서 나온 count값을 밖에서 쓰기위해
    #주어진 범위를 벗어나는 경우에 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 현재노드를 아직 방문하지 않았다면
    if graph[x][y]==1:
        count+=1
        #해당노드 방문처리
        graph[x][y]=0
        #상하좌우의 위치도 모두 재귀적으로 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

result=0
count=0
danji=[]
result=0
for i in range(n):
    for j in range(n):
        #현재위치에서 dfs수행
        if dfs(i,j)==True:
            result+=1
            danji.append(count)
            count=0

print(result)
danji.sort() # 디폴트 오름차순
for d in danji:
    print(d)
