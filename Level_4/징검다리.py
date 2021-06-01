def solution(distance, rocks, n):
    answer = 0
    start, end = 0, distance
    rocks.sort()
    rocks = rocks + [distance]
    while start <= end:
        mid = (start + end) // 2
        temp = 0
        current_rock = 0
        for rock in rocks:
            if rock - current_rock < mid:
                temp += 1
            else:
                current_rock = rock
        if temp > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1

    return answer


print(solution(10, [3, 5, 7], 2))