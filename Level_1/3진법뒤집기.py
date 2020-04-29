def solution(n):
    answer = 0
    temp = []
    while n > 0:
        n, num = divmod(n, 3)
        temp.append(num)
    for i in range(len(temp)):
        answer += temp[i] * (3**(len(temp)-i-1))
    return answer


print(solution(125))
