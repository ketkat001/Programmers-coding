def solution(dartResult):
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    temp = []
    numb = ''
    for dart in dartResult:
        if dart not in number:
            if dart == 'S':
                temp.append(int(numb))
            elif dart == 'D':
                temp.append(int(numb)**2)
            elif dart == 'T':
                temp.append(int(numb)**3)
            elif dart == '*':
                if len(temp) >= 2:
                    temp[-2] *= 2
                temp[-1] *= 2
            elif dart == '#':
                temp[-1] = - temp[-1]
            numb = ''
        else:
            numb += dart
    answer = sum(temp)
    return answer


print(solution('1D2S3T*'))