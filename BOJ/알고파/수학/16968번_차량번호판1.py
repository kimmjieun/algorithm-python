

format = input()
if format[0]=='c':
    sum = 26
else:
    sum = 10
for i in range(1,len(format)):
    if format[i]=='d':
        if format[i]==format[i-1]:
            sum *= 9
        else:
            sum *= 10
    else:
        if format[i]==format[i-1]:
            sum *= 25
        else:
            sum *= 26


print(sum)

