def solution(money):
    n = len(money)
    dp1 = [0] * n
    dp1[0], dp1[1] = money[0], money[0]
    for i in range(2, n-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
    dp1[-1] = dp1[-2]

    dp2 = [0] * n
    dp2[1] = money[1]
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])

    return max(dp1[-1], dp2[-1])


print(solution([1, 2, 3, 1, 5]))