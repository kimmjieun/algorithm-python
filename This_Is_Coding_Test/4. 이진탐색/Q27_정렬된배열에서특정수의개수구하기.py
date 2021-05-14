


from bisect import bisect_left,bisect_right

n,x = map(int,input().split())
array = list(map(int,input().split()))

set_array = set(array)

if x in set_array:
    left = bisect_left(array, x)
    right = bisect_right(array, x)

    print(right - left)
else:
    print(-1)

