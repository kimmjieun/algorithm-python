n = int(input())
for i in range(n):
  star=i+1
  blank=n-i-1
  for k in range(blank):
    print(' ',end='')
  for j in range(star):
    print('*',end='')
  print()