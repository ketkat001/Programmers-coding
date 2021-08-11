def solution(s):
    answer = ''
    numb_dict = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6",
                 "seven": "7", "eight": "8", "nine": "9"}
    numb = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    temp = ''
    for string in s:
        if string in numb:
            answer += string
        else:
            temp += string
        if temp in numb_dict:
            answer += numb_dict[temp]
            temp = ''
    return int(answer)


print(solution("one4seveneight"))