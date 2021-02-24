import sys

# n = int(input())
n = int(sys.stdin.readline())

count = 0

for i in range(n):

    # quiz= input()
    quiz = sys.stdin.readline()

    score = 0
    totalScore = []
    for q in quiz:
        if q == 'O':
            score += 1
        else:
            score = 0

        totalScore.append(score)
    print(sum(totalScore))