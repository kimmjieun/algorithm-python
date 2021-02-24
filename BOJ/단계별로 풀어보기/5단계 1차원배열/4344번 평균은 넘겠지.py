# import sys

c = int(input())
# c = int(sys.stdin.readline())

for i in range(c):
    arr = list(map(int, input().split()))
    # arr = list(map(int,sys.stdin.readline().split()))
    n = arr[0]
    sum = 0
    for i in range(1, n + 1):
        sum += arr[i]
    avg = sum / n

    count = 0
    for i in range(1, n + 1):
        if arr[i] > avg:
            count += 1

    print('%.3f%%' % (round(count / n * 100, 3)))