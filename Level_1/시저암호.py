def solution(s, n):
    answer = ''
    for word in s:
        if word == ' ':
            answer += ' '
        else:
            temp = ord(word) + n
            if temp > 122:
                temp -= 26
            elif 65 <= ord(word) <= 90 and temp > 90:
                temp -= 26
            answer += chr(temp)
    return answer

print(solution("Z", 10))