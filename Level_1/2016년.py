def solution(a, b):
    answer = ''
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0
    for i in range(a-1):
        day += days[i]
    day += b
    if day % 7 == 1:
        answer = 'FRI'
    elif day % 7 == 2:
        answer = 'SAT'
    elif day % 7 == 3:
        answer = 'SUN'
    elif day % 7 == 4:
        answer = 'MON'
    elif day % 7 == 5:
        answer = 'TUE'
    elif day % 7 == 6:
        answer = 'WED'
    elif day % 7 == 0:
        answer = 'THU'
    return answer


print(solution(5, 24))