import sys
N = input()
# N = int(sys.stdin.readline())

originN=N
count=0
while(1):
  sum=0
  for i in N:
    sum+=int(i)
  newN=N[-1]+str(sum)[-1]
  count+=1
  # print(count)
  # print(originN,'|',newN)
  if int(originN)== int(newN):
    break;
  else:
    N=newN
print(count)