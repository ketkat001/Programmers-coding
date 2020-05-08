def solution(n):
    answer = 0
    for i in range(1, n+1):
        start_num = i
        store_num = 0
        while start_num < n+1:
            store_num += start_num
            start_num += 1
            if store_num > n:
                break
            elif store_num == n:
                answer += 1
                break
    return answer


print(solution(15))
