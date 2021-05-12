n = int(input())

arr = list(map(int,input().split()))

# 총 그룹수
result = 0

# 현재 그룹안 인원
group = 0

for a in arr:
    group += 1
    if group>=a:
        result+=1
        group=0

print(result)
