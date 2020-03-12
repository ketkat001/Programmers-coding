def solution(n):
    temp = list(str(n))
    temp.sort(reverse=True)
    answer = int(''.join(temp))
    return answer


print(solution(118372))