def solution(arr):
    arr.remove(min(arr))
    if arr:
        answer = arr
    else:
        answer = [-1]
    return answer


print(solution([4, 3, 2, 1]))