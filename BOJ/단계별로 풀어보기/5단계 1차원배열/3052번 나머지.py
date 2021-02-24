import sys
arr= []
for i in range(10):
  n = int(input())
  # n = int(sys.stdin.readline())
  arr.append(n)

newArr=[]
for i in range(10):
  newArr.append(arr[i]%42)

print(len(list(set(newArr))))