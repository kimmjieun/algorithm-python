import sys

multiply = 1
for i in range(3):
    # n = int(input())
    n = int(sys.stdin.readline())
    multiply *= n

result = [0 for i in range(10)]

for m in str(multiply):
    m = int(m)
    if result[m] == 0:
        result[m] = 1
    else:
        result[m] += 1

for i in result:
    print(i)