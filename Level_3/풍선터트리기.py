def solution(a):
    if len(a) > 2:
        answer = 2
    else:
        return len(a)
    left_min = a[0]
    right_check = {}
    for i in range(1, len(a)-1):
        if a[i] < left_min:
            answer += 1
            left_min = a[i]
        else:
            right_check[a[i]] = 1
    right_min = a[-1]
    for i in range(len(a)-1, -1, -1):
        if a[i] < right_min:
            right_min = a[i]
            if a[i] in right_check:
                answer += 1
    return answer


print(solution([-16, 1, -9]))
