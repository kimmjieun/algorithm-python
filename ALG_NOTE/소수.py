def isPrime(a):
  if a<2:
    return False
  else:
    for i in range(2,a):
      if a%i==0:
        return False
    return True