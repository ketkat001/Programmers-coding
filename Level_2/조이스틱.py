def solution(name):
    answer = 0
    idx = 0
    name = list(name)
    temp = ['A']*len(name)
    while name != temp:
        if name[idx] != 'A':
            q1 = ord(name[idx]) - ord("A")
            q2 = ord("Z") - ord(name[idx]) + 1
            if q1 >= q2:
                answer += q2
            else:
                answer += q1
            name[idx] = 'A'
        else:
            right = 1
            left = 1
            for i in range(1, len(name)):
                if name[idx+i] == 'A':
                    right += 1
                else:
                    break
                if name[idx-i] == 'A':
                    left += 1
                else:
                    break
            if right > left:
                answer += left
                idx -= left
            else:
                answer += right
                idx += right
    return answer


print(solution("BBABAAAB"))