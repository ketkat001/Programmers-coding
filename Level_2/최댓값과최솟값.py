def solution(s):
    answer = ''
    s = list(map(int, s.split(' ')))
    max_num, min_num = max(s), min(s)
    answer = str(min_num) + ' ' + str(max_num)
    return answer


print(solution('-1 -2 -3 -4'))