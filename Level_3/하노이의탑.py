def hanoi(n, start, end, assist, answer):
    if n == 1:
        answer.append([start, end])
        return answer

    answer = hanoi(n-1, start, assist, end, answer)
    answer.append([start, end])
    answer = hanoi(n-1, assist, end, start, answer)
    return answer


def solution(n):
    answer = [] # 원판을 옮기는 순서를 담을 배열
    answer = hanoi(n, 1, 3, 2, answer)
    return answer

print(solution(4))