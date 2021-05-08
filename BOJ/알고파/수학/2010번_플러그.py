# 시간초과
# n = int(input())
#
# arr =[]
# for _ in range(n):
#     arr.append(int(input()))
#
# sum = sum(arr)
#
# print(sum-(len(arr)-1))

# 시간초과
# n = int(input())
# sum=0
# for _ in range(n):
#     sum+=int(input())
#
#
#
# print(sum-(n-1))

import sys
n = int(sys.stdin.readline()) #int(input()) 시간초과
sum=0
for _ in range(n):
    sum+=int(sys.stdin.readline()) #int(input()) 시간초과



print(sum-(n-1))