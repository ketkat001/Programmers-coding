def solution(s):
    answer = []
    s = s.split('},')
    tuple_list = [[] for _ in range(len(s))]
    for i in range(len(s)):
        temp = s[i].replace('{','').replace('}','').split(',')
        for num in temp:
            tuple_list[i].append(int(num))
    tuple_list.sort(key=len)
    for tup in tuple_list:
        for num in tup:
            if num not in answer:
                answer.append(num)

    return answer


print(solution("{{20,111},{111}}"))
