t = int(input())

for i in range(t):
  r,s = input().split()
  r = int(r)
  for j in s:
    print(r*j,end="")
  print() # 이거 안해서 틀림