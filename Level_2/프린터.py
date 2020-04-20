from collections import deque


def solution(priorities, location):
    stand_list = [[] for _ in range(len(priorities))]
    for i in range(len(priorities)):
        stand_list[i] = [priorities[i], i]
    turn = 1
    stand_list = deque(stand_list)
    while stand_list:
        next_print, idx = stand_list.popleft()
        for j in range(len(stand_list)):
            if stand_list[j][0] > next_print:
                stand_list.append([next_print, idx])
                break
        else:
            if idx == location:
                break
            else:
                turn += 1
    answer = turn
    return answer


print(solution([2, 1, 3, 2], 2))