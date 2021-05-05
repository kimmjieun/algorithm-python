# 메모리 초과
# n,m,k = map(int,input().split())
#
# arr = [[0 for col in range(m)] for row in range(n)]
#
# count=0
# for i in range(n):
#     for j in range(m):
#         arr[i][j] = count
#         count +=1
#         # print(i,j,arr[i][j])
#         if arr[i][j] == k:
#             print(i, j) # 사이의 공백 기본적으로 들어가있음
#             break



N, M, K = map(int, input().split())
n = K // M
m = K % M
print(n, m)