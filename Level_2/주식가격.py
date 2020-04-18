def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        temp = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                temp += 1
            else:
                temp += 1
                answer.append(temp)
                break
        else:
            answer.append(temp)

    answer.append(0)
    return answer


print(solution([1, 2, 3, 2, 3]))