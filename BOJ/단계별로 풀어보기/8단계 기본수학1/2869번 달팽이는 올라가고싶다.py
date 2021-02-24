a,b,v=map(int,input().split())

ls=0
if (v-b)%(a-b)!=0:
  ls=((v-b)//(a-b))+1
else:
  ls=((v-b)//(a-b))
print(ls)
# 달팽이는 하루에 a-b만큼 이동
#하지만 목표지점에 도달했을때는 미끄러지지않으므로 v-b만큼올라감