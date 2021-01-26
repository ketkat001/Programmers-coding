def possible(stones, k, mid):
    cnt = 0
    for i in range(len(stones)):
        if stones[i] < mid:
            cnt += 1
        else:
            cnt = 0
        if cnt == k:
            return False
    return True


def solution(stones, k):
    left, right = 1, max(stones) + 1
    while left < right - 1:
        mid = (left+right) // 2
        if possible(stones, k, mid):
            left = mid
        else:
            right = mid
    return left


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))