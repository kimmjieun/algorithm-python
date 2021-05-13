from collections import deque


def bfs():

    queue = deque()
    queue.append(n)
    while queue:
        v = queue.popleft()
        if v == k:
            print(time[v])
            return
        for next_step in (v-1,v+1,v*2):
            if 0<=next_step<max and time[next_step]==0:
                time[next_step]=time[v]+1
                queue.append(next_step)

n,k = map(int,input().split())
max = 100001
time = [0]*max
bfs()