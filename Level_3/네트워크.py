from collections import deque


def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if visited[i]:
            continue
        else:
            visited[i] = 1
            answer += 1
            queue = deque([i])
            while queue:
                current = queue.popleft()
                for i in range(n):
                    if computers[current][i] == 1 and not visited[i]:
                        visited[i] = 1
                        queue.append(i)
    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))