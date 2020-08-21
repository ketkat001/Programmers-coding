def solution(s):
    answer = []
    word_list = list(s.split(' '))
    print(word_list)
    for word in word_list:
        word = word.lower()
        word = word.capitalize()
        answer.append(word)
    answer = ' '.join(answer)
    return answer


print(solution('3people   unFollowed me'))