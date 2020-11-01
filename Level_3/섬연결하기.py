def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    parent = {}
    rank = {}

    def make_set(v):
        parent[v] = v
        rank[v] = 0

    def find(node):
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node_v, node_u):
        root1 = find(node_v)
        root2 = find(node_u)

        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

    for v in range(n):
        make_set(v)

    for cost in costs:
        v, u, weight = cost

        if find(v) != find(u):
            union(v, u)
            answer += weight

    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
