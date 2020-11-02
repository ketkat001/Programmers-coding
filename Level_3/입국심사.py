def binary_search(left, right, n, times):
    answer = float('INF')
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        for time in times:
            cnt += mid // time
        if cnt >= n:
            answer = min(answer, mid)
            right = mid - 1
        else:
            left = mid + 1
    return answer


def solution(n, times):
    answer = binary_search(0, max(times)*n, n, times)
    return answer


print(solution(6, [7, 10]))
