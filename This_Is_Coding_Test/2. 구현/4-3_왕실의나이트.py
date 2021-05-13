# 현재 나이트 위치
input_data = input()

row = int(input_data[1]) # 문자열 두번째 글자
column = int(ord(input_data[0])) - int(ord('a')) +1
# ord 문자에 대한 아스키 코드 값을 반환 , 인덱스 값 계산위해 a의 아스키 코드만큼 뺴주기 , 인덱스 1부터 시작하므로 1 더하기

# steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
steps = [(-2,1),(-2,-1),(-1,-2),(-1,2),(2,1),(2,-1),(1,-2),(1,2)] # 순서는 상관없는듯
result = 0
for step in steps :
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <=8:
        result+=1

print(result)