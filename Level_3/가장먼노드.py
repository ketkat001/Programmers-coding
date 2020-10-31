from collections import deque


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    dp = [0] * (n+1)
    dp[1] = 1
    queue = deque([1])
    for edg in edge:
        graph[edg[0]].append(edg[1])
        graph[edg[1]].append(edg[0])
    while queue:
        answer = len(queue)
        for i in range(answer):
            next_node = queue.popleft()
            for target_node in graph[next_node]:
                if dp[target_node] == 0:
                    dp[target_node] = 1
                    queue.append(target_node)

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))