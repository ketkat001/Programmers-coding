def solution(triangle):
    memo = [[0] * i for i in range(1, len(triangle)+1)]
    memo[-1] = triangle[-1]
    for i in range(len(memo)-2, -1, -1):
        for j in range(i+1):
            memo[i][j] = triangle[i][j] + max(memo[i+1][j], memo[i+1][j+1])
    return memo[0][0]


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))