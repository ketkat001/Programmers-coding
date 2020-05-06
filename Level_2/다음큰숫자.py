def solution(n):
    answer = 0
    number = list(format(n, 'b'))
    count_one = number.count('1')
    while True:
        n += 1
        next_number = list(format(n, 'b'))
        cnt_one = next_number.count('1')
        if count_one == cnt_one:
            answer = n
            break
    return answer


print(solution(78))