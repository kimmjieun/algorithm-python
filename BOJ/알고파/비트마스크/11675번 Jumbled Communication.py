n = int(input())
numbers=list(map(int,input().split()))

for a in numbers:
    for i in range(100001):
        if int(bin(i ^ (i << 1) & 255), 2) == a:
            print(i, end=' ')
            break

