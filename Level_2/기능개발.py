def solution(progresses, speeds):
    answer = []
    while progresses:
        time = 0
        if (100 - progresses[0]) % speeds[0] != 0:
            time += 1
        time += (100 - progresses[0]) // speeds[0]
        for i in range(len(progresses)):
            progresses[i] += speeds[i] * time
        temp, idx = 1, 1
        while idx < len(progresses):
            if progresses[idx] >= 100:
                temp += 1
                idx += 1
            else:
                break
        answer.append(temp)
        progresses = progresses[idx:]
        speeds = speeds[idx:]
    return answer


print(solution([99, 99, 99, 99, 99]	, [3, 3, 3, 3, 3]))