t=int(input())
for _ in range(t):
  k=int(input())
  n=int(input())
  layer0=[i for i in range(1,n+1)]
  for i in range(k):
    for i in range(1,n):
      layer0[i]+=layer0[i-1]
  print(layer0[-1])
