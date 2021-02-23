def isPrime(a):
  if a<2:
    return False
  else:
    for i in range(2,a):
      if a%i==0:
        return False
    return True


n = int(input())
numbers = list(map(int,input().split()))


cnt=0
for i in numbers:
  if isPrime(i):
    cnt+=1
print(cnt)