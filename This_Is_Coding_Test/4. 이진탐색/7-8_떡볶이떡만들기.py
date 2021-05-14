
def binary_search(array, target, start,end):
    #target 떡길이

    if start > end:
        return None

    mid = (start+end)//2
    total = 0
    for i in range(len(array)):
        if array[i]>mid:
            total += array[i]-mid
    if total == target:
        return mid
    elif total > target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array,target,start,mid-1)

n,m = map(int,input().split())

array = list(map(int,input().split()))

end = max(array)

print(binary_search(array, m, 0, end))


