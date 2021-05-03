n = int(input())
lists = []
while True:
    lists.append(n%10)
    n = n // 10
    if n ==0:
        break



lists.sort(reverse=True)

result="".join(map(str,lists))
print(result)
