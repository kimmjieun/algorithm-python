def d(n):
  for i in str(n):
    n+=int(i)
  return n

numbers = set(range(1,10000))

remove_set = set()

for num in numbers:
  remove_set.add(d(num))

self_numbers=numbers - remove_set

for self_num in sorted(self_numbers):
  print(self_num)