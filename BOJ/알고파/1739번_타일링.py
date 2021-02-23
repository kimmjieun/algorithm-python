
def cnt(n):
  fib=[0 for _ in range(n+1)]
  if n ==0 or n==1:
    return 1

  fib[0]=1
  fib[1]=1
  for i in range(2,n+1):
    fib[i]=fib[i-1]+2*fib[i-2]
  return fib[n]


while True:
    try:
        print(cnt(int(input())))
    except:
        break