arr = list(map(int,list(input())))

count1 = 0
count0 = 0


temp = arr[0]
if temp == 1:
    count1=1
else:
    count0=1


for i in range(1,len(arr)):
    if temp == arr[i]:
        continue
    if temp != arr[i]:
        if arr[i]==0:
            count0+=1
        else:
            count1+=1
        temp = arr[i]

print(min(count0,count1))
