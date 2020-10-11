def solution(brown, yellow):
    answer = []
    for i in range(yellow, 0, -1):
        if yellow % i != 0:
            continue
        if (2*i) + (2*(yellow//i)) + 4 == brown:
            answer.append(i+2)
            answer.append(yellow//i+2)
            break
    return answer

print(solution(10, 2))