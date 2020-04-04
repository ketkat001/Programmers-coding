def solution(n):
    answer = '수박'
    if n >= 2:
        if n % 2 == 0:
            temp = n // 2
            answer = '수박' * temp
        else:
            temp = n // 2
            answer = '수박' * temp + '수'
    else:
        answer = answer[:n]
    return answer


print(solution(9))