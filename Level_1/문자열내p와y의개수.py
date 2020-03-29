def solution(s):
    p_cnt, y_cnt = 0, 0
    for i in range(len(s)):
        if s[i] == 'p' or s[i] == 'P':
            p_cnt += 1
        elif s[i] == 'y' or s[i] == 'Y':
            y_cnt += 1
    if p_cnt != y_cnt:
        return False
    return True


print(solution("pPoooyY"))