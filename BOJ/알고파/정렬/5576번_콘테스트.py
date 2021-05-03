Wlist = []
Klist = []
for _ in range(10):
    Wlist.append(int(input()))

for _ in range(10):
    Klist.append(int(input()))

Wlist.sort(reverse=True)
Klist.sort(reverse=True)

sumW=0
for i in range(3):
    sumW+=Wlist[i]

sumK = 0
for i in range(3):
    sumK += Klist[i]

print(sumW,sumK)
