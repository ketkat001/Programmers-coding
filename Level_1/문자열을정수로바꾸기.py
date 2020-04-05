def solution(s):
    if s[0] == '-':
        answer = -int(s[1:])
    elif s[0] == '+':
        answer = int(s[1:])
    else:
        answer = int(s)
    return answer


print(solution('-1234'))
print(solution('1234'))
print(solution('+1234'))