n = int(input())

lists = list(map(int,input().split()))


lists.sort()

sum = 0
for i in range(n):
    sum+=lists[i]*(n-i)

print(sum)