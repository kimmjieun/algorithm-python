S = list(input())

S = list(map(int,S))

S.sort(reverse=True)



if sum(S) == 0:
    print(0)

else:
    result = S[0]
    for i in range(1,len(S)):
        if S[i] <= 1:
            result += S[i]
        else:
            result *= S[i]
    print(result)