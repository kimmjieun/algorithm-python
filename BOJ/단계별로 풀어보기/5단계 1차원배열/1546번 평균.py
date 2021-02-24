import sys

# n = int(input())
n = int(sys.stdin.readline())

# arr = list(map(int,input().split()))
arr = list(map(int,sys.stdin.readline().split()))

maxScore = max(arr)

newArr=[0 for i in range(n)]
for i in range(len(newArr)):
  newArr[i]=arr[i]/maxScore*100

print(sum(newArr)/len(newArr))