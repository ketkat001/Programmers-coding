from collections import deque


def solution(n, path, order):
    answer = True
    graph = [[] for _ in range(n)]
    condition = [0] * n
    visited = [0] * n
    for x, y in path:
        graph[x].append(y)
        graph[y].append(x)
    for x, y, in order:
        condition[y] = x
    if condition[0]:
        return False
    queue = deque([0])
    temp = {}
    while queue:
        cur = queue.popleft()
        next_point = graph[cur]
        for point in next_point:
            if condition[point] != 0 and not visited[condition[point]]:
                temp[condition[point]] = point
                continue
            elif not visited[point]:
                queue.append(point)
                visited[point] = 1
                if point in temp.keys():
                    queue.append(temp[point])
                    visited[temp[point]] = 1
                    del temp[point]
    if sum(visited) != n:
        answer = False

    return answer


print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]]))