s = input() # 하나 입력 받을 땐 이걸로

num =['0','1','2','3','4','5','6','7','8','9']

num_list=[]
alpha_list=[]
for i in s :
    if i in num:
        num_list.append(int(i))
    else :
        alpha_list.append(i)

alpha_list.sort()

result = ''.join(alpha_list)+str(sum(num_list))
print(result)

#K1KA5CB7
#AJKDLSI412K4JSJ9D