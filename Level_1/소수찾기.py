def solution(n):
    answer = 0
    for p in range(2, n+1):
        if dp[p] == 0:
            answer += 1
    return answer


dp = [0] * 1000001
for i in range(2, 1000001):
    cnt = 2
    while True:
        num = i * cnt
        if num > 1000000:
            break
        else:
            cnt += 1
            dp[num] = 1
print(solution(1000000))