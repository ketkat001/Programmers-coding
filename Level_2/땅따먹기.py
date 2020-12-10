def solution(land):
    answer = 0
    row_length = len(land)
    dp = [[0]*4 for _ in range(row_length)]
    dp[0] = land[0]
    for i in range(1, row_length):
        for j in range(4):
            for k in range(4):
                if j != k:
                    dp[i][j] = max(dp[i][j], land[i][j]+dp[i-1][k])
    answer = max(dp[-1])
    return answer


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
