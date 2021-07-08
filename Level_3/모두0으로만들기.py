def solution(a, edges):
    if a.count(0) == len(a):
        return 0
    node_list = {}
    for num in range(len(a)):
        node_list[num] = []
    for edge in edges:
        node_list[edge[0]].append(edge[1])
        node_list[edge[1]].append(edge[0])
    ans = 0
    while node_list:
        for node in node_list.keys():
            if len(node_list[node]) == 1:
                next_node = node_list[node][0]
                node_list[node].pop()
                node_list[next_node].remove(node)
                ans += abs(a[node])
                a[next_node] += a[node]
                a[node] = 0

        del_list = []
        for node in node_list.keys():
            if not node_list[node]:
                del_list.append(node)

        for node in del_list:
            del node_list[node]

    if sum(a) == 0:
        return ans
    return -1

print(solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]))
