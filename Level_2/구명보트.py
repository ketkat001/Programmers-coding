from collections import deque


def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while people:
        person = people.pop()
        weight = limit - person
        if not people:
            answer += 1
            break
        if people[0] <= weight:
            people.popleft()
        answer += 1

    return answer


print(solution([70, 50, 80, 50], 100))