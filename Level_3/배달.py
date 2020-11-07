from collections import deque


def solution(N, road, K):
    answer = 0
    nodes = [[] for _ in range(N+1)]
    dist = [float('inf') for i in range(N+1)]
    dist[1] = 0
    for u, v, d in road:
        nodes[u].append([v, d])
        nodes[v].append([u, d])
    queue = deque([1])
    while queue:
        node = queue.popleft()
        for next_node, d in nodes[node]:
            if dist[next_node] > dist[node] + d:
                dist[next_node] = dist[node] + d
                queue.append(next_node)
    for i in range(1, N+1):
        if dist[i] <= K:
            answer += 1
    return answer


print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))