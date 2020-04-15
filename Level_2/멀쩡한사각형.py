def solution(w, h):
    num1, num2 = max(w, h), min(w, h)
    while True:
        if num1 % num2 == 0:
            temp = num2
            break
        num1, num2 = num2, num1 % num2
    answer = w*h - (w+h-temp)
    return answer


print(solution(3, 4))