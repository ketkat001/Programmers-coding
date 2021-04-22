from collections import deque


def solution(n, signs):
    answer = [[0] * n for _ in range(n)]
    root_list = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if signs[i][j] == 1:
                root_list[i].append(j)

    for i in range(n):
        queue = deque(root_list[i])
        while queue:
            next_stop = queue.popleft()
            if answer[i][next_stop] == 0:
                answer[i][next_stop] = 1
                queue.extend(root_list[next_stop])

    return answer


print(solution(3, [[0, 1, 0], [0, 0, 1], [1, 0, 0]]))