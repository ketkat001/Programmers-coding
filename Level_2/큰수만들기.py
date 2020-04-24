def solution(number, k):
    temp = [number[0]]
    for num in number[1:]:
        while len(temp) > 0 and temp[-1] < num and k > 0:
            k -= 1
            temp.pop()
        temp.append(num)
    if k != 0:
        temp = temp[:-k]
    return ''.join(temp)


print(solution("1234567890"*100000, 999999))