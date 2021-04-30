def insert_word(w_dict, word):
    next_dict = w_dict
    for string in word:
        if string in next_dict:
            next_dict[string][0] += 1
        else:
            next_dict[string] = [1, {}]
        next_dict = next_dict[string][1]
    return w_dict


def solution(words):
    answer = 0
    word_dict = {}
    for word in words:
        word_dict = insert_word(word_dict, word)

    for word in words:
        next_dict = word_dict
        for string in word:
            if next_dict[string][0] != 1:
                answer += 1
            else:
                answer += 1
                break
            next_dict = next_dict[string][1]

    return answer


print(solution(["go", "gone", "guild"]))