n,m,v=map(int,input().split())
matrix=[[0]*(n+1) for i in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    matrix[a][b]=matrix[b][a]=1

visit_list=[0]*(n+1)

def dfs(v):

    visit_list[v]=1 # 방문했다는 표시
    print(v,end=' ') # 출력
    for i in range(1,n+1):
        if visit_list[i]==0 and matrix[v][i]==1: #방문하지않은 노드이면서 연결된 노드일때
            dfs(i)


def bfs(v):
    queue=[v] #들려야할 정점 저장
    visit_list[v]=0 #방문한점 0으로 표시 위에서 1로바꿔놔서 여기선 0으로 표기
    while queue:
        v=queue.pop(0) #첫번째 데이터 pop
        print(v,end=' ') #
        for i in range(1,n+1):
            if(visit_list[i]==1 and matrix[v][i]==1):
                queue.append(i)
                visit_list[i]=0

dfs(v)
print()
bfs(v)