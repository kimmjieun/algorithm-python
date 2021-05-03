import sys
n = int(input())

lists = []
for _ in range(n):
    a,b = input().split()
    a=int(a)
    lists.append([a,b])


lists.sort(key=lambda x : x[0])

for i in range(n):
    print(lists[i][0],lists[i][1])
