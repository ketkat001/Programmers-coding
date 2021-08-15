def solution(scores):
    n = len(scores)
    my_scores = [[] for i in range(n)]
    avg_score = [0] * n
    for score in scores:
        for i in range(n):
            my_scores[i].append(score[i])

    for j in range(n):
        my_score = my_scores[j][j]
        if (my_score == max(my_scores[j]) or my_score == min(my_scores[j])) and my_scores[j].count(my_score) == 1:
            my_scores[j].remove(my_score)

    for p in range(n):
        avg_score[p] = sum(my_scores[p]) // len(my_scores[p])
    answer = ''
    for score in avg_score:
        if score >= 90:
            answer += 'A'
        elif score >= 80:
            answer += 'B'
        elif score >= 70:
            answer += 'C'
        elif score >= 50:
            answer += 'D'
        else:
            answer += 'F'
    return answer


print(solution([[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [47, 88, 95, 80, 67],
                [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]))