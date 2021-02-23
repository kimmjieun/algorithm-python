m= int(input())
n= int(input())

def isPrime(a):
  if a<2:
    return False
  else:
    for i in range(2,a):
      if a%i==0:
        return False
    return True

nums=[]
for i in range(m,n+1):
  if isPrime(i):
    nums.append(i)

if not nums:
  print(-1)
else:
  print(sum(nums))
  print(min(nums))