def solution(s):
    word_list = s.split(" ")
    answer = ''
    for word in word_list:
        temp = ''
        for i in range(len(word)):
            if i % 2 == 0:
                temp += word[i].upper()
            else:
                temp += word[i].lower()
        answer += temp + ' '
    return answer[:-1]


print(solution("try hello world"))