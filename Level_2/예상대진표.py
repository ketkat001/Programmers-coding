def solution(n, a, b):
    answer = 1
    while True:
        if abs(a-b) == 1 and (a+b-3)%4 == 0:
            break
        else:
            answer += 1
            a = (a+1)//2
            b = (b+1)//2
    return answer


print(solution(8, 4, 7))

