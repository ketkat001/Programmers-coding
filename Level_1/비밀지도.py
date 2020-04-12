def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        s1 = format(arr1[i], 'b').zfill(n)
        s2 = format(arr2[i], 'b').zfill(n)
        temp = ''
        for j in range(n):
            if s1[j] == s2[j]:
                if s1[j] == '0':
                    temp += ' '
                else:
                    temp += '#'
            else:
                temp += '#'
        answer.append(temp)
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))