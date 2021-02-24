n = int(input())
man=[]
for _ in range(n):
  man.append(list(map(int,input().split())))

man_len=len(man)

seq=[]
for i in range(man_len):
  cnt = 1
  for j in range(man_len):
    if man[i][0] < man[j][0] and man[i][1] < man[j][1]:
      cnt+=1
  seq.append(cnt)
for i in seq:
  print(i,end=' ')