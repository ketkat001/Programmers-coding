def solution(matrix_sizes):
    n = len(matrix_sizes)
    dp = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0
    for num in range(1, n):
        for start in range(n-1):
            end = start + num
            if end >= n:
                break
            for k in range(start, end):
                dp[start][end] = min(dp[start][end], dp[start][k] + dp[k+1][end] +
                                     (matrix_sizes[start][0] * matrix_sizes[k][1] * matrix_sizes[end][1]))
    answer = dp[0][n-1]
    return answer


print(solution([[5, 3], [3, 10], [10, 6]]))
