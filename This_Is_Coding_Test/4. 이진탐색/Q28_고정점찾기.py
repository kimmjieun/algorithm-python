import sys
def binary_search(array,start,end):
    # 고정점이 없는경우를 나타냄
    if start > end:
        return None

    mid = (start+end)//2


    if array[mid]==mid:
        return mid
    elif array[mid]>mid: # 1<2
        return binary_search(array,start,mid-1)
    else: # array[mid]<mid:
        return binary_search(array,mid+1,end)





n = int(sys.stdin.readline().rstrip())
array = list(map(int,sys.stdin.readline().rstrip().split()))


result = binary_search(array,0,n-1)

if result == None:
    print(-1)
else:
    print(result)

