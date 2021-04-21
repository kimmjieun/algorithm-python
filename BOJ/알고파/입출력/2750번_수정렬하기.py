n = int(input())

lists = []
for _ in range(n):
    a = int(input())
    lists.append(a)

lists.sort()

for list in lists:
    print(list)