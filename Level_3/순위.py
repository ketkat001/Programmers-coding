def solution(n, results):
    answer = 0
    win = [set([]) for _ in range(n+1)]
    lose = [set([]) for _ in range(n+1)]
    for i in range(len(results)):
        win[results[i][1]].add(results[i][0])
        lose[results[i][0]].add(results[i][1])

    for i in range(1, n+1):
        for j in win[i]:
            lose[j].update(lose[i])

        for k in lose[i]:
            win[k].update(win[i])

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            answer += 1

    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))