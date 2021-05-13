n = int(input())

dic={}
for _ in range(n):
  tmp = int(input())
  if tmp in dic:
    dic[tmp]+=1
  else:
    dic[tmp]=1
dic = sorted(dic.items(),key=lambda x:(-x[1], x[0]))
# 카드개수를 기준으로 먼저 내림차순으로 정렬후 카드개수가 같으면 카드값을 기준으로 오름차순 정렬되게 구현했다
# x[1]-밸류는 내림차순 x[0] - 키는 오름차순 (-x[1], x[0]) 1순위 밸류 2순위 키

print(dic[0][0])