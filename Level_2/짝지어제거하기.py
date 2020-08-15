def solution(s):
    answer = 0
    s = list(s)
    stack = []
    while s:
        word = s.pop()
        if stack and stack[-1] == word:
            stack.pop()
        else:
            stack.append(word)
    if stack:
        return 0
    return 1


print(solution('baabaa'))
