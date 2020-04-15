def solution(n, m):
    answer = []
    if n >= m:
        num1, num2 = n, m
    else:
        num1, num2 = m, n
    while True:
        if num1 % num2 == 0:
            answer.append(num2)
            break
        else:
            num1, num2 = num2, num1 % num2
    answer.append(num2*(n//num2)*(m//num2))
    return answer




print(solution(3, 12))