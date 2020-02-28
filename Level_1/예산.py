def solution(d, budget):
    answer = 0
    d.sort()
    temp = 0
    for i in range(len(d)):
        temp += d[i]
        if temp <= budget:
            answer += 1
        else:
            break
    return answer


print(solution([1,3,2,5,4], 9))