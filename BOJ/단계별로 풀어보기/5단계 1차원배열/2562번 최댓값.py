import sys

lists=[]
for i in range(9):
  # n = int(input())
  n = int(sys.stdin.readline())
  lists.append(n)

maxN=max(lists)
print(max(lists))
for i in range(9):
  if int(maxN)==int(lists[i]):
    print(i+1)
    break