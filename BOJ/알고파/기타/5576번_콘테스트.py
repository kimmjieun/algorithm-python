
list1=[]
list2=[]
for i in range(10):
  list1.append(int(input()))

for i in range(10):
  list2.append(int(input()))

list1.sort(reverse=True) #내림차순
list2.sort(reverse=True) #내림차순

print(sum(list1[:3]),sum(list2[:3]))