def solution(s):
    check_list = list(s)
    stack = []
    while True:
        if not check_list:
            break
        temp = check_list.pop()
        if temp == '(':
            if stack:
                temp_check = stack.pop()
                if temp == temp_check:
                    return False
            else:
                return False
        else:
            stack.append(temp)
    if stack:
        return False
    return True

print(solution("()()"))