def cal_decimal(number, n):
    result = ''
    while number >= n:
        num = number % n
        if num >= 10:
            num += 55
            result += chr(num)
        else:
            result += str(num)
        number = number // n
    if number >= 10:
        number += 55
        result += chr(number)
    else:
        result += str(number)
    return list(result[::-1])


def solution(n, t, m, p):
    answer = ''
    turn = 1
    for num in range(t*m):
        decimal_num = cal_decimal(num, n)
        for numb in decimal_num:
            if turn == p:
                answer += numb
            turn += 1
            if turn > m:
                turn = 1
            if len(answer) == t:
                break
        if len(answer) == t:
            break
    return answer


print(solution(16, 16, 2, 1))