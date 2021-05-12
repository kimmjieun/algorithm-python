n,m = map(int,input().split())

min_arr=[]

# 나)
# arr=[]
# for i in range(n):
#     arr.append(list(map(int,input().split())))
# for i in range(n):
#     min_arr.append(min(arr[i]))
# print(max(min_arr))

# 참고)
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    max_value=max(result,min(data))
print(max_value)

