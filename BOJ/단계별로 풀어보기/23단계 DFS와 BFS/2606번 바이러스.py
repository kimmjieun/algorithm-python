n = int(input())
m = int(input())

matrix=[[0]*(n+1) for i in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    matrix[a][b]=matrix[b][a]=1

visit_list=[1]*(n+1)

def bfs(v):
    count=0
    queue=[v] #들려야할 정점 저장
    visit_list[v]=0
    while queue:
        v=queue.pop(0) #첫번째 데이터 pop
        count+=1
        # print(v,end=' ') #
        for i in range(1,n+1):
            if(visit_list[i]==1 and matrix[v][i]==1):
                queue.append(i)
                visit_list[i]=0
    return count-1

print(bfs(1))