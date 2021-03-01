#시간초과
# m = int(input())
#
# S=set() #집합자료형
# for _ in range(m):
#     tmp = input().split()
#
#     if len(tmp)==1:
#         if tmp[0]=='all':
#             s=set([i for i in range(1,21)])
#         else:
#             s=set()
#         continue
#     a,b=tmp[0],int(tmp[1])
#
#     if a=='add':
#         S.add(b)
#
#     if a=='remove':
#         S.discard(b)
#
#     if a=='toggle' and b in S:
#         S.discard(b)
#     elif a=='toggle' and b not in S:
#         S.add(b)
#
#     if a=='check' and b in S:
#         print(1)
#     elif a=='check' and b not in S:
#         print(0)

# 집합 으로 선언
# 길이 1일때 먼저 처리
# input 대신 sys
# remove 대신 discard
# 체크일때 정규식

#정답
import sys

s = set()
n = int(input())

for i in range(n):
    tmp = sys.stdin.readline().strip().split()

    if len(tmp) == 1:  # command만 있을 경우
        if tmp[0] == 'all':
            s = set([i for i in range(1, 21)])
        else:
            s = set()
        continue

    # command와 target이 존재할 때
    command, target = tmp[0], tmp[1]
    target = int(target)

    if command == 'add':
        s.add(target)
    elif command == 'check':
        print(1 if target in s else 0)
    elif command == 'remove':
        s.discard(target)
    elif command == 'toggle':
        if target in s:
            s.discard(target)
        else:
            s.add(target)