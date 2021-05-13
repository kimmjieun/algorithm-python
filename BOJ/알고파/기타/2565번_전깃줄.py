
n = int(input())

line=[list(map(int,input().split())) for _ in range(n)]
line.sort(key=lambda x :x[0])
dp=[0]*501

for s, d in line:
  dp[d]=max(dp[:d])+1

print(n-max(dp))