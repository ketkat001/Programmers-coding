from collections import deque


def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n, m = len(maps), len(maps[0])
    queue = deque([[0, 0, 1]])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    while queue:
        x, y, cnt = queue.popleft()
        if [x, y] == [n-1, m-1]:
            answer = cnt
            break
        for d in range(4):
            next_x, next_y, next_cnt = x + dx[d], y + dy[d], cnt + 1
            if 0 <= next_x < n and 0 <= next_y < m and not visited[next_x][next_y] and maps[next_x][next_y]:
                queue.append([next_x, next_y, next_cnt])
                visited[next_x][next_y] = 1
    if answer == 0:
        return -1
    return answer


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))