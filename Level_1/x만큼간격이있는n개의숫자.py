def solution(x, n):
    answer = []
    temp = x
    while n > 0:
        answer.append(temp)
        temp += x
        n -= 1
    return answer


print(solution(2, 5))