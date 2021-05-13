# import sys
# score = sys.stdin.readline() #1234입력시에 줄개수세보면 개행문자 포함되어서 5 출력
score = input()

length = len(score)//2 # 소수점 제거
left = list(map(int,list(score[:length])))
right = list(map(int,list(score[length:])))

if sum(left) == sum(right):
    print('LUCKY')
else :
    print('READY')

