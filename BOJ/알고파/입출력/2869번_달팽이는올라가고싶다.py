# a,b,v = map(int,input().split())
#
# sum =0
# count=0
# while True:
#     count += 1
#     sum += a
#     if sum>=v:
#         break
#     sum -= b
#
# print(count)

# 위 아마 시간초과

import math
a,b,v = map(int,input().split())
count = (v-b)/(a-b)
print(math.ceil(count))