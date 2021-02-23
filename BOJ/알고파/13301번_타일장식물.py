n = int(input())

dp = [0]*81

dp[0]=1
dp[1]=1

for i in range(2,n):
  dp[i] = dp[i-1]+dp[i-2]

r = dp[n-1] + dp[n-1] + dp[n-2]

print( r+r )