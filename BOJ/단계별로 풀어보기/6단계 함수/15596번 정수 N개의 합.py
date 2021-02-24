def solve(a):
  sum = 0
  for i in a:
    sum+=i
  return sum


a = list(map(int,input().split()))
solve(a)