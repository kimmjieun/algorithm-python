import sys

# t = int(input())
t = int(sys.stdin.readline())

for i in range(t):
  # n = int(input())
  n = int(sys.stdin.readline())
  # memo1 = list(map(int,input().split()))
  memo1 = set(map(int,sys.stdin.readline().split()))

  # m = int(input())
  m = int(sys.stdin.readline())
  # memo2 = list(map(int,input().split()))
  memo2 = list(map(int,sys.stdin.readline().split()))

  for m2 in memo2:
    if m2 in memo1:
      print(1)
    else:
      print(0)