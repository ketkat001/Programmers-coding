def solution(n, s, a, b, fares):
    pay_dp = [[float('inf')] * (n+1) for _ in range(n+1)]
    for fare in fares:
        pay_dp[fare[0]][fare[1]] = fare[2]
        pay_dp[fare[1]][fare[0]] = fare[2]

    for l in range(1, n+1):
        pay_dp[l][l] = 0

    for p in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                pay_dp[i][j] = min(pay_dp[i][j], pay_dp[i][p] + pay_dp[p][j])

    min_pay = float('inf')
    for k in range(1, n+1):
        taxi_pay = pay_dp[s][k] + pay_dp[k][a] + pay_dp[k][b]
        if min_pay > taxi_pay:
            min_pay = taxi_pay

    return min_pay

print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))

