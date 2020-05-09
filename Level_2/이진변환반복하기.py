def solution(s):
    zero_cnt, cnt = 0, 0
    while s != '1':
        zero_cnt += s.count('0')
        s = s.replace('0', '')
        num = s.count('1')
        s = format(num, 'b')
        cnt += 1
    answer = [cnt, zero_cnt]
    return answer


print(solution("110010101001"))