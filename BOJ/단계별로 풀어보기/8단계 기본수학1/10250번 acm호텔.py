t=int(input())
for _ in range(t):
  h,w,n=map(int,input().split())
  if n%h==0:
    layer=str(h)
    room=str(n//h).zfill(2)
  else:
    layer=str(n%h)
    room=str(n//h+1).zfill(2)
  print(layer+room)