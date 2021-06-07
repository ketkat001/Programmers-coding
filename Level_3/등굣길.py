def solution(m, n, puddles):
    dp_list = [[0]*(m+1) for _ in range(n+1)]
    dp_list[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                dp_list[i][j] = 0
            else:
                dp_list[i][j] = dp_list[i-1][j] + dp_list[i][j-1]
    return dp_list[n][m]


print(solution(4, 3, [[2, 2]]))