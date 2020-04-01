def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    for word in s:
        if ord(word) < 48 or ord(word) > 57:
            return False
    return True


print(solution("1234"))