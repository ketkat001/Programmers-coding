def solution(str1, str2):
    word1_list, word2_list = {}, {}
    for i in range(len(str1)-1):
        word = str1[i:i+2].lower()
        if word.isalpha():
            if word not in word1_list:
                word1_list[word] = 1
            else:
                word1_list[word] += 1

    for j in range(len(str2)-1):
        word = str2[j:j+2].lower()
        if word.isalpha():
            if word not in word2_list:
                word2_list[word] = 1
            else:
                word2_list[word] += 1

    word_union, word_dif = 0, 0
    for key, value in word1_list.items():
        if key in word2_list:
            word_union += max(value, word2_list[key])
            word_dif += min(value, word2_list[key])
        else:
            word_union += value

    for key, value in word2_list.items():
        if key not in word1_list:
            word_union += value

    if word_union == 0 and word_dif == 0:
        answer = 65536
    else:
        answer = int(word_dif/word_union*65536)
    return answer


print(solution('FRANCE', 'french'))