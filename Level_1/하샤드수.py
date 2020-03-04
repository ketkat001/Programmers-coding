def solution(x):
    answer = True
    num = str(x)
    temp = 0
    for n in num:
        temp += int(n)
    if x % temp != 0:
        return False
    return answer


print(solution(10))