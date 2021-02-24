import sys

# n = int(input())
n = int(sys.stdin.readline())

# lists = list(map(int,input().split()))
lists = list(map(int,sys.stdin.readline().split()))

print('%d %d'%(min(lists),max(lists)))