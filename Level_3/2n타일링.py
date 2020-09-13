def solution(n):
    answer = 0
    if n < 3:
        return n
    a, b = 1, 2
    for i in range(3, n+1):
        answer = (a+b)
        a = b
        b = answer

    return answer%1000000007


print(solution(500))