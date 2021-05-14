# 리스트안에 해당원소가 포홤되는지 확인하여 풀었지만 , 이진탐색단원이므로 이진탐색으로 풀어보겠다.


# 이함수는 외울 것
def binary_search(array,target,start,end):
    if start > end:
        return None

    mid = (start+end)//2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)


m = int(input())
array = list(map(int,input().split()))
array.sort()

n = int(input())
customer = list(map(int,input().split()))

for i in range(n):
    result = binary_search(array,customer[i],0,m-1)
    if result == None:
        print('no',end=' ')
    else:
        print('yes',end=' ')