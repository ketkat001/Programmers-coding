def solution(a, b):
    distance = abs(a-b)+1
    temp, repeat = a+b, distance//2
    if distance % 2 == 0:
        answer = temp * repeat
    else:
        answer = temp * repeat + temp // 2

    return answer


print(solution(3, 5))