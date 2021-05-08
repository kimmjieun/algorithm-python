import sys
import collections
t = int(sys.stdin.readline())

for _ in range(t):
    num = int(sys.stdin.readline())

    su = 2  # 검사할 첫 값
    so = []  # 소인수 저장할 리스트 변수

    while su <= num:  # 검사 값이 num보다 작은 동안
        if num % su == 0:  # 나머지가 없으면
            so.append(su)  # 소인수 리스트에 추가
            num //= su  # num을 검사 값으로 나눔
        else:  # 나머지 있는 경우엔
            su += 1  # 검사 값 1 증가

    # print(so)  # 소인수 리스트 출력
    dict = collections.Counter(so)
    for key in dict:
        print(key, dict[key])




