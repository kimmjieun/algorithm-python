
N,M = map(int,input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arrays = arr1+arr2
arrays.sort(reverse=False)
for i in arrays:
  print( i, end=' ')