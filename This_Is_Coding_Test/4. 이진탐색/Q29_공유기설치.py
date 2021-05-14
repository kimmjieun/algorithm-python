n,c = map(int,input().split())

array=[]
for _ in range(n):
    array.append(int(input()))

array.sort()

start =1 # 가능한 최소거리
end = array[-1]-array[0] # 가능한 최대거리

result = 0

while(start<=end):
    mid = (start+end)//2 # mid = 가장 인접한 두 공유기 사이의 거리
    # 첫째집에는 무조건 공유기를 설치한다고 가정
    value=array[0]
    count = 1
    # 현재 mid 값을 이용해 공유기를 설치하기
    for i in range(1,n):
        if array[i] >= value+mid:
            value=array[i]
            count+=1
    if count>=c:
        start=mid+1
        result=mid
    else:
        end=mid-1

print(result)