def solution(n, lost, reserve):
    answer = n - len(lost)
    temp = []
    for stu in lost:
        if stu in reserve:
            answer += 1
            reserve.remove(stu)
            temp.append(stu)
            continue
    for num in temp:
        lost.remove(num)
    for stu in lost:
        if stu - 1 in reserve:
            answer += 1
            reserve.remove(stu-1)
        elif stu + 1 in reserve:
            answer += 1
            reserve.remove(stu+1)
    return answer


print(solution(3, [1, 2], [2, 3]))