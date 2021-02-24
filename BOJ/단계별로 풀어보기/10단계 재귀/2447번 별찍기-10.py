def stars(star_lst):
    new_star_lst = []
    for i in range(3 * len(star_lst)):
        if i // len(star_lst) == 1:
            new_star_lst.append(star_lst[i % len(star_lst)] + " " * len(star_lst) + star_lst[i % len(star_lst)])
        else:
            new_star_lst.append(star_lst[i % len(star_lst)] * 3)
    return list(new_star_lst)

star = ["***", "* *", '***']
n = int(input())
iter = 0
while n != 3:
    n = int(n / 3)
    iter += 1

for i in range(iter):
    star = stars(star)
for i in star:
    print(i)