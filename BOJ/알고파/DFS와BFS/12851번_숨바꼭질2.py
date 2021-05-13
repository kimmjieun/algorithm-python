from collections import deque

n,k = map(int,input().split())
max = 100001


queue = deque()
queue.append(n)

cnt =0
time = [-1]*max
time[n]=0

while queue:
    v = queue.popleft()
    if v == k:
        cnt+=1
    for next_step in (v-1,v+1,v*2):
        if 0<=next_step<max:
            if time[next_step]>=time[v]+1 or time[next_step]==-1: #방문한적없거나 현재시간 +1인경우
                time[next_step]=time[v]+1
                queue.append(next_step)


print(time[k])
print(cnt)




