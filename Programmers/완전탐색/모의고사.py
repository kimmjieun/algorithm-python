def solution(answers):
    men1 = [1, 2, 3, 4, 5]
    men2 = [2, 1, 2, 3, 2, 4, 2, 5]
    men3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]
    for idx, ans in enumerate(answers):
        if ans == men1[idx % len(men1)]:
            score[0] += 1
        if ans == men2[idx % len(men2)]:
            score[1] += 1
        if ans == men3[idx % len(men3)]:
            score[2] += 1

    result = []
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx + 1)

    return result


answer = [1, 2, 3, 4, 5]
print(solution(answer))
