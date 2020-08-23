def solution(msg):
    answer = []
    word_dictionary = {}
    for i in range(1, 27):
        word_dictionary[i] = chr(64+i)
    k = 0
    while k < len(msg):
        for i in range(len(word_dictionary), 0, -1):
            compare_word = word_dictionary[i]
            compare_word_length = len(compare_word)
            if compare_word == msg[k:k+compare_word_length]:
                word_dictionary[len(word_dictionary) + 1] = msg[k:k + compare_word_length + 1]
                k += compare_word_length
                answer.append(i)
                break
    return answer


print(solution('KAKAO'))