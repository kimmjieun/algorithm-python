n,m = map(int,input().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    # 주어진 범위 벗어나는경우 즉시 종료
    if x <=-1 or x>=n or y <= -1 or y>=m:
        return False
    # 현재노드를 아직 방문하지 않았다면
    if graph[x][y]==0:
        graph[x][y]=1 # 방문처리
        # 상하좌우 위치도 모두 재귀적으로 호출
        dfs(x-1,y) # 상
        dfs(x,y-1) # 좌
        dfs(x+1,y) # 하
        dfs(x,y+1) # 우
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1
print(result)


